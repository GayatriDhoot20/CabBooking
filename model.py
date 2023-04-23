class Customer:
    def __init__(self, lastName, firstName, mobileNo, emailId, userName, password, id=None):
        self.id = id
        self.last_name = lastName
        self.first_name = firstName
        self.mobile_no = mobileNo
        self.email_id = emailId
        self.user_name = userName
        self.password = password

    def get_mobile_no(self):
        return self.mobile_no


class Driver:
    def __init__(self, lastName, firstName, mobileNo, emailId, vehicalNo, vehicalName, adharNo, userName,
                 password, id=None):
        self.id = id
        self.last_name = lastName
        self.first_name = firstName
        self.mobile_no = mobileNo
        self.email_id = emailId
        self.vehical_no = vehicalNo
        self.vehical_name = vehicalName
        self.adhar_no = adharNo
        self.user_name = userName
        self.password = password

    def get_user_name(self):
        return self.user_name

    def get_mobile_no(self):
        return self.mobile_no

    def get_adhar_no(self):
        return self.adhar_no