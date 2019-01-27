#!/usr/bin/python
# -*- coding:utf-8

# import MySQLdb(python3废弃)
import time,traceback,logging
import pymysql

class DBOperateAction:
    def __init__(self,dbhost,dbaccount,dbpasswd,dbname,port=3306,charset='utf8'):
        self.dbhost = dbhost
        self.dbaccount = dbaccount
        self.dbpasswd = dbpasswd[::-1]
        self.dbname = dbname
        self.port = port
        self.charset = charset
        self.db_conn = ""
        self.db_cursor = ""

    def connect(self):
        try:
            self.db_conn = pymysql.connect(host=self.dbhost,user=self.dbaccount,passwd=self.dbpasswd,
            db=self.dbname,port=self.port,charset=self.charset,connect_timeout=5)
            self.db_cursor = self.db_conn.cursor()
            return True
        except pymysql.OperationalError:
            logging.error("Connect to"+self.dbhost+"Faild")
            logging.exception("exception message:")
            return False


    def re_connect(self):
        logging.error("connect to mysql server failed reconnect")
        try:
            self.db_conn = pymysql.connect(host=self.dbhost,user=self.dbaccount,passwd=self.dbpasswd,
            db=self.dbname,port=self.port,charset="utf8")
            self.db_cursor = self.db_conn.cursor()
            return True
        except pymysql.OperationalError:
            logging.error("Reconnect MySQL failed")
            return False


    def get_all_result(self,sql):
        try:
            logging.info("Execute sql:"+sql)
            self.db_cursor.execute(sql)
            self.db_conn.commit()
            result = self.db_cursor.fetchall()
            return result
        except pymysql.OperationalError:
            for i in range(0,3):
                time.sleep(5)
                if self.re_connect():
                    logging.info("reconnect to"+self.dbhost+"database successfully")
                    return False
        except pymysql.ProgrammingError:
            logging.exception("exception message:")
            return False


    def get_one_result(self,sql):
        try:
            logging.info("Execute sql:"+sql[:500])
            self.db_cursor.execute(sql)
            self.db_conn.commit()
            result = self.db_cursor.fetchone()
            return result
        except pymysql.OperationalError:
            traceback.print_exc()
            for i in range(0,3):
                time.sleep(5)
                if self.re_connect():
                    self.db_cursor.execute(sql)
                    self.db_conn.commit()
                    result = self.db_cursor.fetchone()
                    logging.warning("Reconnect to "+self.dbhost+" successfully")
                    return result
                return False

    def close_connection(self):
        self.db_conn.close()

# if __name__=="__main__":
#
#     host = "10.100.157.68"
#     db_account = "jfmysql"
#     db_passwd = "7tTQMnUIpT9E"
#     db_name = "tcbiz_financer"
#
#     db_operation = DBOperateAction(host,db_account,db_passwd,db_name,port=3306)
#     db_operation.connect()
#     select_sql = "SELECT memberId FROM `ThirdPartyAcct` WHERE thirdPartyCode='0006' AND openFlag=1 AND spPartner='50000'"
#     print(select_sql)
#
#     result = db_operation.get_all_result(select_sql)
#     db_operation.close_connection()
#     print(result)

# MySQLdb.connect 建立和MySQL 数据库的连接
# • cursor=conn.cursor() 通过上一步建立的连接获取个cursor
# 对象
# • cursor.execute（sql) 执行SQL 语句， 但返回结果不是SQL
# 执行的结果，是此SQL 执行后收影响的行数
# • cursor.fetchall（）： 获取SQL 执行的所有结果，返回
# 结果是个嵌套的元组
# • cursor.fetchall（）获取SQL 执行的结果，只获取第一条
# • cursor.close() ， conn.close() ： 关闭连接和cursor