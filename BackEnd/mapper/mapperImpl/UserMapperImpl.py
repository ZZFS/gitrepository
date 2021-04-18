from BackEnd.mapper.UserMapper import UserMapper
from BackEnd.model.User import User
from BackEnd.util.db_utils import DbUtils

utils = DbUtils()
Session = utils.getSession()

class UserMapperImpl(UserMapper):
    def addUser(self, name, password):
        user_obj = User(name=name, password=password)  # 生成你要创建的数据对象
        # 将创建的对象添加到session中
        Session.add(user_obj)  # 把要创建的数据对象添加到这个session里，一会统一创建
        Session.commit()  # commit之后，才统一提交，创建数据

    def updateUser(self):
        my_user = Session.query(User).filter(User.id == 1).first()  # 得到查询的结果的，并且返回一个对象
        my_user.name = 'Jack'  # 面向对象赋值

    def SearchUser(self):
        my_user = Session.query(User).filter(User.id == 1).first()
        print(my_user)

    def deletUser(self,name):
        # 删：
        Session.query(User).filter(User.name==name).delete()
        Session.commit()
