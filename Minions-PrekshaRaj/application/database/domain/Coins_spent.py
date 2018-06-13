from flywheel import Model, Field, Engine, NUMBER, STRING
from datetime import datetime


class Minion_Coins_spent(Model):
    feedId = Field(data_type=NUMBER, range_key = True)
    userId = Field(data_type=STRING, hash_key = True)
    coinAmt = Field(data_type=NUMBER)
    brandId = Field(data_type=NUMBER)
    spentOn = Field(data_type=STRING) #mark if the coin was spent on item or minion
    spentId = Field(data_type=STRING) #id of item or minion on which coin was spent
    date = Field(data_type=datetime)
    
    def __init__(self, feedId, userId, coinAmt, brandId, spentOn, date):
        super(Minion_Coins_spent, self).__init__()
        self.feedId = feedId
        self.userId = userId
        self.coinAmt = coinAmt
        self.brandId = brandId
        self.spentOn = spentOn
        self.date = date
