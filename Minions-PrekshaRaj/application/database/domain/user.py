from datetime import datetime

from flywheel.fields.types import DateTimeType

from flywheel import Model, Field, Engine,set_

from dynamo3 import (Binary, NUMBER, STRING, BINARY, NUMBER_SET, STRING_SET,
                     BINARY_SET, BOOL, MAP, LIST)


class Minion_User(Model):
    userId = Field(data_type=STRING, hash_key=True)
    userName = Field(data_type=STRING, range_key=True)
    TrainingStatusID = Field(data_type=set_(NUMBER))
    password = Field(data_type=STRING)
    name = Field(data_type=STRING)
    dob = Field(data_type=datetime)
    gender = Field()
    phoneNumber = Field()
    email = Field()
    address = Field()
    city = Field()
    state = Field()
    country = Field()
    date_signup = Field(data_type=datetime)
    last_accessed_date = Field(data_type=NUMBER, index='ts-index')
    is_active = Field(data_type=NUMBER)
    secret_token = Field(data_type=STRING)
    secret_token_exp = Field(data_type=NUMBER)
    client_ip = Field(data_type=STRING)
    signuptype = Field(data_type=STRING)

    def __init__(self, userid='', username='', password='', email=''):
        super(Minion_User, self).__init__()
        self.userId = userid
        self.userName = username
        self.password = password
        self.email = email

    #list of attributes that are sent to user, when user info is retrieved
    user_attr = ['userName','name','dob','gender','phoneNumber','email','address',\
    'city','state','country','date_signup','last_accessed_date', 'is_active', 'signuptype']