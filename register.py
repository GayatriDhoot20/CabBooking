class Register:
    def __init__(self, mydb, mycursor, userObj):
        self.mydb = mydb
        self.mycursor = mycursor
        self.user_obj = userObj

    def register_customer(self):
        sql = f"insert into customer values (NULL,'{self.user_obj.last_name}','{self.user_obj.first_name}','{self.user_obj.mobile_no}','{self.user_obj.email_id}','{self.user_obj.user_name}','{self.user_obj.password}');"
        self.mycursor.execute(sql)
        self.mydb.commit()
        self.mycursor.close()

        # self.mydb.close_connection(self)

    def register_driver(self):
        sql = "insert into driver values (NULL,%s,%s,%s,%s,%s,%s)"
        val = (self.user_obj.last_name, self.user_obj.first_name, self.user_obj.mobile_no,
               self.user_obj.email_id,  self.user_obj.user_name, self.user_obj.password)
        self.mycursor.execute(sql, val)
