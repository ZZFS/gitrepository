from abc import ABCMeta, abstractmethod

from BackEnd.model.User import User
from BackEnd.util.db_utils import DbUtils

utils = DbUtils()
Session = utils.getSession()
class UserMapper(object):
    __metaclass__ = ABCMeta #指定这是一个抽象类
    @abstractmethod  #抽象方法
    def addUser(self, name, password):
        pass
    # @abstractmethod  # 抽象方法
    def updateUser(self):
        pass
    # @abstractmethod  # 抽象方法
    def SearchUser(self):
        pass
    # @abstractmethod  # 抽象方法
    def deletUser(self,name):
        pass
