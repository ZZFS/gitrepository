import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker  # 创建表数据的时候使用的模块

engine = create_engine("mysql+pymysql://mrli:liyuan+123@rm-8vb9665iy4k8g096ilo.mysql.zhangbei.rds.aliyuncs.com:3306/qframe_mysql", encoding='utf-8', echo=True)


class DbUtils:
    def getSession(self):
        # 创建表数据：
        Session_class = sessionmaker(bind=engine)  # 创建与数据库会话的session class，注意这里返回给session的是一个class，不是实例
        Session = Session_class()  # 生成session实例
        return Session

    def getBase(self):
        Base = declarative_base()  # 生成orm基类
        return Base
