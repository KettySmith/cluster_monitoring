from .init import search_blue
from flask import request
import pymysql

# 创建连接
db = pymysql.connect(host='localhost', user='tester', password='test', port=3306)
# 创建游标
cursor = db.cursor()


# 相似度比对
@search_blue.route("/similarity_search", methods=['POST'])
def similarity_search():
    input_json = request.get_json(force=True)
    rank = input_json['rank']  # top10=>rank=10  top5=>rank=5
    start_time = input_json['start_time']  # 开始时间
    end_time = input_json['end_time']  # 截止时间
    # 相似度分析
    res = process_similarity(rank, start_time, end_time)
    #todo: 处理结果
    return res


# 相似度分析函数
def process_similarity(rank: str, start_time: str, end_time: str):
    return None, None


if __name__ == '__main__':
    database_sql = "USE cc_cc408_hya"
    cursor.execute(database_sql)
    db.commit()
