# from .init import search_blue
from flask import request
import pymysql
from dtw import *

# 创建连接
db = pymysql.connect(host='localhost', user='tester', password='test', port=3306)
# 创建游标
cursor = db.cursor()


# 相似度比对
# @search_blue.route("/similarity_search", methods=['POST'])
def similarity_search():
    input_json = request.get_json(force=True)
    print(input_json)
    rank = int(input_json['rank'])  # top10=>rank=10  top5=>rank=5
    ab_node = str(input_json['ab_node'])    # 异常数据表名
    start_time = str(input_json['start_time'])  # 开始时间
    end_time = str(input_json['end_time'])  # 截止时间
    # 相似度分析
    res = process_similarity(rank, ab_node, start_time, end_time)
    #todo: 处理结果
    return res


# 相似度分析函数
def process_similarity(rank: int, ab_node:str, start_time: str, end_time: str):
    # 返回值：根据rank返回一个list，元素为相似度从高到低的<node_name:simi_value>
    # simi_value：dtw算法算出的距离，距离越大表示相似度越低 

    # 得到表名
    nodes_name = get_similarity_node()
    # 得到异常序列和对比序列列表
    ret = get_similarity_data(nodes_name, ab_node, start_time, end_time)
    nodes_name.remove(ab_node)
    query = ret.pop(ab_node)
    refers = ret

    simi_list = []
    while(len(refers)):
        curr_node = nodes_name.pop()
        refer = refers.pop(curr_node)
        # dtw算法对比两个序列的相似度
        alignment = dtw(x=query['y_data_list'], 
                        y=refer['y_data_list'],
                        dist_method="euclidean",
                        step_pattern=asymmetric,
                        keep_internals=True)
        # alignment.plot(type="twoway", offset=1, ylab=curr_node)
        # 将相似度分析结果加入list
        node_simi = dict()
        node_simi['node_name'] = curr_node
        node_simi['simi_value'] = alignment.__getattribute__('distance')
        node_simi['x_data_list'] = refer['x_data_list']
        node_simi['y_data_list'] = refer['y_data_list']
        simi_list.append(node_simi)
    # 按相似度大小排序，只返回rank个最相似序列
    simi_list.sort(key=lambda e:e['simi_value'])
    simi_list = simi_list[:rank]
    return simi_list


# 获取相似度比对的数据表名
def get_similarity_node(filename="AIBMA-ES-CLUSTER-20230423"):
    database_name = filename.replace("-", "_")
    database_sql = "USE " + database_name
    cursor.execute(database_sql)
    db.commit()
    res = []
    # 查询表名
    sql = "select table_name from information_schema.tables where table_schema='AIBMA_ES_CLUSTER_20230423' order by cast(substr(table_name,9,length(table_name)) as signed ) asc;"
    cursor.execute(sql)
    ret = cursor.fetchall()
    for item in ret:
        res.append(item[0])
    return res


# 根据输入的表名获取相似度信息
def get_similarity_data(nodes_name:list, ab_node:str, start_time:str, end_time:str):
    database_sql = "USE AIBMA_ES_CLUSTER_20230423"
    cursor.execute(database_sql)
    db.commit()
    res = dict()
    # 根据需要查询的节点名称去查询
    for node_name in nodes_name:
        res[node_name] = dict()
        datas = select_node_similarity_data(node_name, ab_node == node_name, start_time, end_time)
        res[node_name]['x_data_list'] = datas[0]
        res[node_name]['y_data_list'] = datas[1]
    return res


# 从表中截取序列
def select_node_similarity_data(table_name:str, isQuery:bool, start_time:str, end_time:str):
    # 找到开始序列的首尾id
    sql = "select id from " + table_name + " where date=\'" + start_time +"\' or date=\'" + end_time +"\'"
    cursor.execute(sql)
    datas = cursor.fetchall()
    start_id, end_id = datas[0][0], datas[1][0]
    
    sql = "select id,date,value from " + table_name + " where date!=''" 
    cursor.execute(sql)
    datas = cursor.fetchall()
    x_data_list = []
    y_data_list = []
    # 对于对比序列，考虑波动提前/延后的情况，将对比时间段边界放宽
    for data in datas:
        if(not isQuery and data[0] >= start_id-2 and data[0] < start_id):
            x_data_list.append(data[1])
            y_data_list.append(float(data[2]))
        elif(data[0] >= start_id and data[0] <= end_id):
            x_data_list.append(data[1])
            y_data_list.append(float(data[2]))
        elif(not isQuery and data[0] > end_id and data[0] <= end_id + 2):
            x_data_list.append(data[1])
            y_data_list.append(float(data[2]))
        elif(data[0] > end_id+2):
            break
    return x_data_list, y_data_list


if __name__ == '__main__':
    process_similarity(5, 'abnormal0', '2023/4/23 15:20', '2023/4/23 17:20')

