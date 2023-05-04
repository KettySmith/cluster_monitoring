from .init import upload_blue
import os
import pymysql
import csv

# 创建连接
db = pymysql.connect(host='localhost', user='tester', password='test', port=3306)
# 创建游标
cursor = db.cursor()


@upload_blue.route("/upload_all_files", methods=['POST'])
def upload_all_files(all_file_root_input: str = "2套集群数据"):
    # 获取数据集所在路径
    # root = os.path.dirname(os.path.dirname(os.getcwd()))
    root = os.path.dirname(os.getcwd())
    # 所有文件的根路径
    all_file_root = os.path.join(root, all_file_root_input)
    print(all_file_root)
    # 遍历当前目录下的所有目录
    file_root_list = os.listdir(all_file_root)
    for file_root in file_root_list:
        # 导入每一个目录（集群）的数据
        print("start")
        if (os.path.isdir(os.path.join(all_file_root, file_root))):
            upload_each_file(file_root, os.path.join(all_file_root, file_root))
        print("finish")
    return "success"


def upload_each_file(cluster_name: str, file_root_path: str):
    # 若数据库不存在，则根据集群名称创建数据库
    create_database(cluster_name)
    # 每个文件建立一张数据库表，递归创建
    dfs_create_table(file_root_path)


def create_database(database_name: str):
    database_name = database_name.replace("-", "_")
    print(database_name)
    # 创建数据库的sql(如果数据库存在就不创建，防止异常)
    sql = "CREATE DATABASE IF NOT EXISTS " + database_name + ""
    # 执行创建数据库的sql
    print(sql)
    cursor.execute(sql)
    db.commit()
    # 使用当前数据库
    sql = "USE " + database_name
    cursor.execute(sql)
    db.commit()


def dfs_create_table(file_root_path: str):
    count = 0
    for path, file_dir, files in os.walk(file_root_path):
        if count == 1:
            break
        # 为文件，创建数据表
        for file_name in files:
            # 创建数据表，并返回插入语句
            insert_sql = create_table(file_name, os.path.join(file_root_path, file_name))
            # 插入数据
            insert_data(insert_sql, os.path.join(file_root_path, file_name))
        # 为目录，递归创建
        for dir in file_dir:
            dfs_create_table(os.path.join(file_root_path, dir))
        count += 1


def create_table(table_name: str, file_path: str):
    if table_name.find(".") != -1 and table_name.find("==") != -1:
        table_name = table_name.split(".")[0].split("==")[1]
    elif table_name.find(".") != -1:
        table_name = "abnormal" + table_name.split(".")[0]
    drop_sql = "DROP TABLE IF EXISTS " + table_name
    cursor.execute(drop_sql)
    db.commit()
    # 获取csv文件第一行
    print(file_path)
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
        header = result[0]
    create_sql = "CREATE TABLE `%s` (`id` int(11) NOT NULL AUTO_INCREMENT," % table_name
    for i in header:
        create_sql += "`%s` varchar(255) DEFAULT NULL," % i
    create_sql += "PRIMARY KEY (`id`)) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;"
    cursor.execute(create_sql)
    db.commit()
    insert_sql = "insert into %s(%s)values(%s)" % (table_name, ",".join(header), ",".join(['%s'] * len(header)))
    return insert_sql


def insert_data(insert_sql: str, file_path: str):
    csv_file = open(file_path, encoding='utf-8')
    csv_reader_lines = csv.reader(csv_file)

    insert_datas = []
    for index, i in enumerate(csv_reader_lines):
        if index == 0:
            continue
        sql_data = tuple(i)
        insert_datas.append(sql_data)
        if index + 1 % 1000 == 0:
            cursor.executemany(insert_sql, insert_datas)
            db.commit()
            insert_datas = []

    if len(insert_datas) != 0:
        cursor.executemany(insert_sql, insert_datas)
        db.commit()


if __name__ == '__main__':
    database_name = "cc-cc408-hya"
    database_name = database_name.replace("-", "_")
    print(database_name)
