# @Time : 2021/1/14 20:18
# @Author : XX
# @File : DBHelper.py
# @Project : QFrame
# @Software : PyCharm
import pymysql


class DBHelper:
    def __init__(self, host=None, port=None, user=None, password=None, charset='utf8', database=None):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.charset =charset
        self.database =database

    # 数据库连接
    def connectMySQL(self):
        '''初始化参数'''
        conn = pymysql.connect(host=self.host,  # 域名
                               port=self.port,  # 端口号
                               user=self.user,  # 数据库登陆的用户名
                               password=self.password,  # 数据库登陆的用户名
                               charset=self.charset,  # 是utf-8
                               database=self.database,  # 你要连接的那个数据库
                              )
        return conn

    def query_all(self, sql, args=None):
        '''查询所有数据库语句'''
        conn = self.connectMySQL()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return result

    def query_one(self,sql,args=None):
        '''查询一条数据库语句'''
        conn = self.connectMySQL()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()
        return result

    def query_all(self, sql, args=None):
        '''查询所有数据库语句'''
        conn = self.connectMySQL()
        cursor = conn.cursor()
        cursor.execute(sql, args)
        result = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        return result

if __name__ == '__main__':
    db = DBHelper("rm-8vb9665iy4k8g096ilo.mysql.zhangbei.rds.aliyuncs.com", 3306, "ly_mysql", "liyuan+123", 'utf8', "liyuan_mysql")
    print(db.query_one("select * from book"))