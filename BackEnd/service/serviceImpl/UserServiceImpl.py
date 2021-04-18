from BackEnd.mapper.mapperImpl.UserMapperImpl import UserMapperImpl
from BackEnd.model.User import User
from BackEnd.service.UserService import UserService
from BackEnd.util.db_utils import DbUtils

utils = DbUtils()
Session = utils.getSession()

class UserServiceImpl(UserService):
    def __init__(self):
        self.userMapper = UserMapperImpl()

    def addUser(self, name, password):
        pass

    def deletUser(self, name):
        pass

    def updateUser(self):
        pass

    def SearchUser(self):
        return self.userMapper.SearchUser()


