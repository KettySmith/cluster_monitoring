from .init import search_blue
from flask import request
import os
import pymysql

# 创建连接
db = pymysql.connect(host='localhost', user='tester', password='test', port=3306)
# 创建游标
cursor = db.cursor()

@search_blue.route("/simirity_search", methods=['POST'])
def simirity_search():
    return

if __name__ == '__main__':
    database_sql = "USE cc_cc408_hya"
    cursor.execute(database_sql)
    db.commit()