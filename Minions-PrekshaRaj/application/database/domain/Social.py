
from flywheel import Model, Field, NUMBER, STRING, Composite


class Minion_Social(Model):

    userId = Field(data_type = STRING)
    type = Field(data_type = STRING)
    socialId = Composite('userId','type',hash_key=True)
    userName = Field(data_type = STRING)
    token = Field(data_type = STRING)

    def __init__(self, userId, type, userName, token):
    	super(Minion_Social, self).__init__()
        self.userId = userId
        self.type = type
        self.userName = userName
        self.token = token
