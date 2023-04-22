class users:
    def __init__(self,id,lastname,firstname,mobileno,city,username,password):
        self.id = id
        self.lastname=lastname
        self.firstname=firstname
        self.mobileno=mobileno
        self.city=city
        self.username=username
        self.password=password

    def getid(self):
        return self.id

    def getMobileno(self):
        return self.mobileno