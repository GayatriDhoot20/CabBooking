from mysqlconnect import Mysql
class usercontroller:
    __connection=None

    def __init__(self):
        self.__connection=Mysql.connect()

    def __isvalidLogin(self, users):
        if users.getMobileno()!="":
            return True
        return False

    def __Authorize(self):
        pass
pass


u = usercontroller()
print(Mysql.message)