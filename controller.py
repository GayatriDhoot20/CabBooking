from mysqlconnect import Mysql
from model import Customer, Driver
from register import Register


class UserController:
    def __init__(self):
        self.myconnect = Mysql
        self.mydb = self.myconnect.connect()
        self.mycursor = self.mydb.cursor(buffered=True)

    # def __init__(self):
    #     self.__connection=Mysql.connect()

    # def __isvalidLogin(self, users):
    #     if users.getMobileno()!="":
    #         return True
    #     return False
    #
    # def __Authorize(self):
    #     pass

    def get_user_info(self):
        user_obj = int(input("Please pree 1 for Customer and 2 for Driver"))
        if user_obj == 1:
            last_name = input("Please enter last name")
            first_name = input("Please enter first name")
            mobile_number = input("Please enter Mobile number")
            email_id = input("Please enter mail id")
            user_name = input("Please enter user name")
            password = input("Please enter password")

            user_obj = Customer(last_name, first_name, mobile_number, email_id, user_name, password)
            res = Register(self.mydb, self.mycursor, user_obj)
            res.register_customer()
        else:
            last_name = input("Please enter last name")
            first_name = input("Please enter fisrst name")
            mobile_number = input("Please enter Mobile number")
            email_id = input("Please enter mailid")
            vehicalNo = input("Please enter vehical number")
            vehicalName = input("Please enter vehical name")
            adharNo = input("Please enter adhar number")
            user_name = input("Please enter user name")
            password = input("Please enter password")
            driver_obj = Driver(1, last_name, first_name, mobile_number, email_id, vehicalNo, vehicalName, adharNo,
                                user_name, password)
            res = Register(self.mydb, self.mycursor, driver_obj)
            res.register_driver()


u = UserController()
u.get_user_info()
