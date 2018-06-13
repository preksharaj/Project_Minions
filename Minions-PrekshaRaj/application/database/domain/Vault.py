from flywheel import Model, Field, Engine, NUMBER, STRING
from datetime import datetime


class Minion_Vault(Model):
    brandId = Field(data_type=NUMBER, range_key = True)
    userId = Field(data_type=STRING, hash_key = True)
    coinAmt = Field(data_type=NUMBER)
    lastChangeDate = Field(data_type=datetime,index='ts_index')
    # uid = Composite('userId','quantity', data_type=STRING, merge=score_merge,range_key=True)

    def __init__(self, brandId, userId, coinAmt, lastChangeDate):
        super(Minion_Vault, self).__init__()
        self.brandId = brandId
        self.userId = userId
        self.coinAmt = coinAmt
        self.lastChangeDate = lastChangeDate
