from flywheel import Model, Field, Engine, NUMBER, STRING
from datetime import datetime


class Minion_Shop(Model):
    shopId = Field(data_type=NUMBER, hash_key = True)
    shop_name = Field(data_type=STRING)
    shop_description = Field(data_type=STRING)
    mapped_toBrand = Field(data_type=NUMBER)
    date_added = Field(data_type=datetime)

    def __init__(self, shopId, shop_name, shop_description, mapped_toBrand, date_added):
        super(Minion_Shop, self).__init__()
        self.shopId = shopId
        self.shop_name = shop_name
        self.shop_description = shop_description
        self.mapped_toBrand = mapped_toBrand
        self.date_added = date_added
