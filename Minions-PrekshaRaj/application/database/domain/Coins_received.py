from flywheel import Model, Field, Engine, NUMBER, STRING
from datetime import datetime


class Minion_Coins_received(Model):
    transactionId = Field(data_type=NUMBER, range_key = True)
    userId = Field(data_type=STRING, hash_key = True)
    coinAmt = Field(data_type=NUMBER)
    brandId = Field(data_type=NUMBER)
    reason = Field()
    received_from = Field()
    date = Field(data_type=datetime)
    
    def __init__(self, transactionId, userId, coinAmt, brandId, date):
        super(Minion_Coins_received, self).__init__()
        self.transactionId = transactionId
        self.userId = userId
        self.coinAmt = coinAmt
        self.brandId = brandId
        self.date = date
