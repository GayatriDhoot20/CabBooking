import mysql.connector

class Mysql:
    message = ""
    @staticmethod
    def connect():
        try:
            mydb = mysql.connector.connect(host="localhost", user="root",passwd="",database="cabbooking_system")

            if mydb.is_connected():
                Mysql.message="connected"
                # print("connected")
                return mydb
        except Exception as e:
            Mysql.message=e

    def close_connection(self,connection):
        connection.close()

Mysql.connect()
print(Mysql.message)


