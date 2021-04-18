# @Time : 2021/2/22 15:52
# @Author : XX
# @File : TestController.py
# @Project : QFrame
# @Software : PyCharm
from BackEnd.service.serviceImpl.UserServiceImpl import UserServiceImpl

userService = UserServiceImpl()
# userService.deletUser("李广源")
print(userService.SearchUser())
# u=User("zzfs","zzfs")
# print(u.__repr__())
