import time
import pymysql
import threading
from DBUtils.PooledDB import PooledDB, SharedDBConnection
POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=1024,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=8,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
    maxcached=16,  # 链接池中最多闲置的链接，0和None不限制
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    maxusage=None,  # 一个链接最多被重复使用的次数，None表示无限制
    setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
    ping=0,
    # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
    host='rm-cn-lbj37bbhw0012n9o.rwlb.rds.aliyuncs.com',
    port=3306,
    user='root',
    password='SOFT_test'
)

def get_con_cursor():
    conn = POOL.connection()
    cursor = conn.cursor()

    return conn,cursor

def sql_end(conn,cursor):
    cursor.close()
    conn.close()
