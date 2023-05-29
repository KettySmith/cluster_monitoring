from .init import show_blue
from flask import request
import pymysql
from soft.sql.connect_pool import *


@show_blue.route("/choose_cluster/<cluster_name>", methods=['GET'])
def choose_cluster(cluster_name: str):
    # 根据传入的集群名称，查找对应的数据库，获取每类指标的结点数量
    cluster_name = cluster_name.replace("-", "_")
    database_sql = "USE " + cluster_name
    con, cursor = get_con_cursor()
    cursor.execute(database_sql)
    res = dict()
    # 集群层面指标数据
    # elasticsearch_cluster_health_active_shards
    res['elasticsearch_cluster_health_active_shards'] = []
    # elasticsearch_cluster_health_number_of_nodes
    res['elasticsearch_cluster_health_number_of_nodes'] = []
    # elasticsearch_cluster_health_status
    res['elasticsearch_cluster_health_status'] = []
    # 节点层面单指标数据
    # elasticsearch_indices_indexing_index_time_seconds_total
    res['elasticsearch_indices_indexing_index_time_seconds_total'] = select_single_node(
        "elasticsearch_indices_indexing_index_time_seconds_total", cursor)
    # elasticsearch_indices_search_query_time_seconds
    res['elasticsearch_indices_search_query_time_seconds'] = select_single_node(
        "elasticsearch_indices_search_query_time_seconds", cursor)
    # elasticsearch_os_load5
    res['elasticsearch_os_load5'] = select_single_node(
        "elasticsearch_os_load5", cursor)
    # elasticsearch_process_cpu_percent
    res['elasticsearch_process_cpu_percent'] = select_single_node(
        "elasticsearch_process_cpu_percent", cursor)
    # elasticsearch_transport_rx_size_bytes_total
    res['elasticsearch_transport_rx_size_bytes_total'] = select_single_node(
        "elasticsearch_transport_rx_size_bytes_total", cursor)
    # elasticsearch_transport_tx_size_bytes_total
    res['elasticsearch_transport_tx_size_bytes_total'] = select_single_node(
        "elasticsearch_transport_tx_size_bytes_total", cursor)
    # 节点层面多指标数据
    # elasticsearch_filesystem_data_available_bytes
    res['elasticsearch_filesystem_data_available_bytes'] = select_multi_node(
        "elasticsearch_filesystem_data_available_bytes", cursor)
    # elasticsearch_jvm_gc_collection_seconds_sum
    res['elasticsearch_jvm_gc_collection_seconds_sum'] = select_multi_node(
        "elasticsearch_jvm_gc_collection_seconds_sum", cursor)

    sql_end(con, cursor)
    return res


# 集群层面
@show_blue.route("/get_cluster_data/<cluster_name>", methods=['GET'])
def get_cluster_data(cluster_name: str):
    cluster_name = cluster_name.replace("-", "_")
    database_sql = "USE " + cluster_name
    con, cursor = get_con_cursor()
    cursor.execute(database_sql)
    res = dict()
    # 集群层面指标数据
    # elasticsearch_cluster_health_active_shards
    res['elasticsearch_cluster_health_active_shards'] = dict()
    ret = select_cluster_data("elasticsearch_cluster_health_active_shards", cursor)
    res['elasticsearch_cluster_health_active_shards']['x_data_list'] = ret[0]
    res['elasticsearch_cluster_health_active_shards']['y_data_list'] = ret[1]
    # elasticsearch_cluster_health_number_of_nodes
    res['elasticsearch_cluster_health_number_of_nodes'] = dict()
    ret = select_cluster_data("elasticsearch_cluster_health_number_of_nodes", cursor)
    res['elasticsearch_cluster_health_number_of_nodes']['x_data_list'] = ret[0]
    res['elasticsearch_cluster_health_number_of_nodes']['y_data_list'] = ret[1]
    # elasticsearch_cluster_health_status
    res['elasticsearch_cluster_health_status'] = dict()
    ret = select_cluster_data("elasticsearch_cluster_health_status", cursor)
    res['elasticsearch_cluster_health_status']['x_data_list'] = ret[0]
    res['elasticsearch_cluster_health_status']['y_data_list'] = ret[1]

    sql_end(con, cursor)
    return res


# 单节点单指标
@show_blue.route("/get_node_single_data/<cluster_name>/<metric_name>", methods=['POST'])
def get_node_single_data(cluster_name: str, metric_name: str):
    nodes_name = list(request.values.getlist("nodes_name"))
    cluster_name = cluster_name.replace("-", "_")
    database_sql = "USE " + cluster_name
    con, cursor = get_con_cursor()
    cursor.execute(database_sql)
    res = dict()
    # 根据需要查询的节点名称去查询
    for node_name in nodes_name:
        res[node_name] = dict()
        datas = select_node_single_data(metric_name, node_name, cursor)
        res[node_name]['x_data_list'] = datas[0]
        res[node_name]['y_data_list'] = datas[1]

    sql_end(con,cursor)
    return res


# 单节点多指标
@show_blue.route("/get_node_multi_data/<cluster_name>/<metric_name>", methods=['POST'])
def get_node_multi_data(cluster_name: str, metric_name: str):
    nodes_name = list(request.values.getlist("nodes_name"))
    cluster_name = cluster_name.replace("-", "_")
    database_sql = "USE " + cluster_name
    con, cursor = get_con_cursor()
    cursor.execute(database_sql)
    res = dict()
    # 根据需要查询的节点名称去查询
    for node_name in nodes_name:
        res[node_name] = dict()
        datas = select_node_multi_data(metric_name, node_name, cursor)
        res[node_name]['x_data_list'] = datas[0]
        res[node_name]['y_data_list'] = datas[1]

    sql_end(con,cursor)
    return res


# 获取相似度比对的数据表名
@show_blue.route("/get_similarity_node", methods=['GET'])
def get_similarity_node(filename="AIBMA-ES-CLUSTER-20230423"):
    database_name = filename.replace("-", "_")
    database_sql = "USE " + database_name
    con,cursor = get_con_cursor()
    cursor.execute(database_sql)
    res = []
    # 查询表名
    sql = "select table_name from information_schema.tables where table_schema='AIBMA_ES_CLUSTER_20230423' order by cast(substr(table_name,9,length(table_name)) as signed ) asc;"
    cursor.execute(sql)
    ret = cursor.fetchall()
    for item in ret:
        res.append(item[0])

    sql_end(con,cursor)
    return res


# 根据输入的表名获取相似度信息
@show_blue.route("/get_similarity_data", methods=['POST'])
def get_similarity_data():
    nodes_name = list(request.values.getlist("nodes_name"))
    database_sql = "USE AIBMA_ES_CLUSTER_20230423"
    con,cursor = get_con_cursor()
    cursor.execute(database_sql)
    res = dict()
    # 根据需要查询的节点名称去查询
    for node_name in nodes_name:
        res[node_name] = dict()
        datas = select_node_similarity_data(node_name,cursor)
        res[node_name]['x_data_list'] = datas[0]
        res[node_name]['y_data_list'] = datas[1]
    return res


def select_node_similarity_data(table_name,cursor):
    sql = "select date,value from " + table_name + " where date!='' and value!=''"
    print(sql)
    cursor.execute(sql)
    datas = cursor.fetchall()
    x_data_list = []
    y_data_list = []
    for data in datas:
        x_data_list.append(data[0])
        y_data_list.append(data[1])
    return x_data_list, y_data_list


def select_single_node(table_name, cursor):
    # 查询节点
    sql = "select distinct node_name from " + table_name + " order by node_name asc"
    cursor.execute(sql)
    nodes = cursor.fetchall()
    res_nodes = []
    for node in nodes:
        res_nodes.append(node[0])
    return res_nodes


def select_multi_node(table_name, cursor):
    # 根据不同指标，查询不同数据表，拼接不同节点名称
    if table_name == "elasticsearch_filesystem_data_available_bytes":
        sql = "select distinct concat(concat(node_name,'---'),mount) as new_node_name from " + table_name + " order by new_node_name asc"
    elif table_name == "elasticsearch_jvm_gc_collection_seconds_sum":
        sql = "select distinct concat(concat(node_name,'---'),gc) as new_node_name from " + table_name + " order by new_node_name asc"
    cursor.execute(sql)
    nodes = cursor.fetchall()
    res_nodes = []
    for node in nodes:
        res_nodes.append(node[0])
    return res_nodes


def select_cluster_data(table_name, cursor):
    sql = "select date,value from " + table_name
    cursor.execute(sql)
    datas = cursor.fetchall()
    x_data_list = []
    y_data_list = []
    for data in datas:
        x_data_list.append(data[0])
        y_data_list.append(data[1])
    return x_data_list, y_data_list


def select_node_single_data(table_name, node_name, cursor):
    sql = "select date,value from " + table_name + " where node_name = %s"
    cursor.execute(sql, node_name)
    datas = cursor.fetchall()
    x_data_list = []
    y_data_list = []
    for data in datas:
        x_data_list.append(data[0])
        y_data_list.append(data[1])
    return x_data_list, y_data_list


def select_node_multi_data(table_name, node_name, cursor):
    if table_name == "elasticsearch_filesystem_data_available_bytes":
        sql = "select date,value from " + table_name + " where concat(concat(node_name,'---'),mount) = %s"
    elif table_name == "elasticsearch_jvm_gc_collection_seconds_sum":
        sql = "select date,value from " + table_name + " where concat(concat(node_name,'---'),gc) = %s"
    cursor.execute(sql, node_name)
    datas = cursor.fetchall()
    x_data_list = []
    y_data_list = []
    for data in datas:
        x_data_list.append(data[0])
        y_data_list.append(data[1])
    return x_data_list, y_data_list

