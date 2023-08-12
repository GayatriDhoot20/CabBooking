from math import radians, cos, sin, asin, sqrt


class User:
    customer = []

    def __init__(self, id, name=None, mobile_number=None, mail_id=None, username=None,
                 password=None, logitude=None, latitude=None):  # constructor
        self.id = id
        self.name = name
        self.mobile_numer = mobile_number
        self.mail_id = mail_id
        self.username = username
        self.password = password
        self.logitude = logitude
        self.latitude = latitude

    def register(self):
        self.customer.append(
            {"id": self.id, "name": self.name, "mobile_number": self.mobile_numer, "mail_id": self.mail_id,
             "user_name": self.username, "password": self.password, "logitude": self.logitude,
             "latitude": self.latitude})
        return self.customer

    def login(self, username, password):
        for sub in self.customer:
            if sub['user_name'] == username and sub['password'] == password:
                return "Login sucessfully"
            else:
                return "Username doesn't exists please enter correct username"


class Driver(User):
    driver = []

    def __init__(self, id, name=None, mobile_number=None, mail_id=None, username=None, password=None, logitude=None,
                 latitude=None, licencedetails=None, vehical_number=None, vehical_type=None, is_assigned=None):
        super().__init__(id, name, mobile_number, mail_id, username, password, logitude, latitude)
        self.licencedetails = licencedetails
        self.vehical_number = vehical_number
        self.vehical_type = vehical_type
        self.is_assigned = is_assigned

    def register(self):
        self.driver.append(
            {"id": self.id, "name": self.name, "mobile_number": self.mobile_numer, "mail_id": self.mail_id,
             "user_name": self.username, "password": self.password, "latitude": self.latitude,
             "longitude": self.logitude, "licencedetails": self.licencedetails,
             "vehical_number": self.vehical_number, "vehical_type": self.vehical_type,"is_assigned":self.is_assigned})
        return self.driver

    def login(self, username, password):
        for sub in self.driver:
            if sub['user_name'] == username and sub['password'] == password:
                return "Login sucessfully"
            else:
                return "Username doesn't exists please enter correct username"


class Ride:
    def __init__(self, customer_obj, driver_obj, source, destination):
        self.customer_obj = customer_obj
        self.driver_obj = driver_obj
        self.source = source
        self.destination = destination

    def book_ride(self):
        pass


obj1 = User(1, 'gayatri', '9876543210', 'gdhoot202@gmail.com', 'gdhoot',
            'pass', '18.6298', '73.7997')
obj1.register()
obj2 = User(2, 'gauri', '9876543210', 'garis2202@gmail.com', 'gauris',
            'pass1', '18.4529', '73.8652')
obj2.register()

obj3 = Driver(1, 'driver1', '9087654320', 'jambhulwadi', 'driver1',
              'pass', '18.4268', '73.8397', 'ABCD1234',
              'MH-12 GS2022', 'Car',False)
obj3.register()
obj3 = Driver(1)
obj3.login('driver1', 'pass')
obj2.login("gdhoot", "pass")
longitude = obj2.logitude
latitude = obj2.latitude


def dist(lat1, long1, lat2, long2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
    # haversine formula
    dlon = long2 - long1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    km = 6371 * c
    print(km)
    return km


for i in obj3.driver:
    distance = dist(float(latitude), float(longitude), float(i['latitude']), float(i['longitude']))
    if distance <= 5:
        driver_assigned = i
        i['is_assigned'] = True
        print(driver_assigned)
    else:
        print("nearby driver not found")
