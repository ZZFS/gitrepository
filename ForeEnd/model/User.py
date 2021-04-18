import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker  # 创建表数据的时候使用的模块

from BackEnd.util.db_utils import DbUtils
engine = create_engine("mysql+pymysql://mrli:liyuan+123@rm-8vb9665iy4k8g096ilo.mysql.zhangbei.rds.aliyuncs.com:3306/qframe_mysql", encoding='utf-8', echo=True)

utils = DbUtils()
Base = utils.getBase()


class User(Base):
    __tablename__ = 't4'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def __repr__(self):
        return "<id='%s',name='%s',password='%s'>" % (self.id, self.name, self.password)


Base.metadata.create_all(engine)  # 执行创建表结构的sql sqlalchemy会将对象转化为SQL语句
