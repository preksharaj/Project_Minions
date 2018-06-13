from flywheel import Model, Field, Engine, NUMBER, STRING
from datetime import datetime


class Minion_Sharing(Model):
    shareId = Field(data_type=NUMBER, range_key = True)
    to_userId = Field(data_type=STRING, hash_key = True)
    from_userId = Field(data_type=STRING)
    type = Field(data_type=STRING)
    amount = Field(data_type=NUMBER)
    sent_via = Field(data_type=STRING)
    sent_date = Field(data_type=datetime,index='ts_index')
    
    def __init__(self, shareId, to_userId, from_userId, type, amount, sent_via, sent_date):
        super(Minion_Sharing, self).__init__()
        self.shareId = shareId
        self.to_userId = to_userId
        self.from_userId = from_userId
        self.type = type
        self.amount = amount
        self.sent_via = sent_via
        self.sent_date = sent_date
