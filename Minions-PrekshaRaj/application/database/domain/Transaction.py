from flywheel import Model, Field, Engine, NUMBER, STRING
from datetime import datetime


class Minion_Transaction(Model):
    transactionId = Field(data_type=NUMBER, range_key = True)
    userId = Field(data_type=STRING, hash_key = True)
    shopId = Field(data_type=NUMBER)
    purchase_date = Field(data_type=datetime)
    amount = Field(data_type=NUMBER)
    payment_method = Field(data_type=STRING)
    added_ToVault = Field(data_type=NUMBER)

    def __init__(self, transactionId, userId, shopId, purchase_date, amount, payment_method, added_ToVault):
        super(Minion_Transaction, self).__init__()
        self.transactionId = transactionId
        self.userId = userId
        self.shopId = shopId
        self.purchase_date = purchase_date
        self.amount = amount
        self.payment_method = payment_method
        self.added_ToVault = added_ToVault
