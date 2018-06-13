
from flywheel import Model, Field, NUMBER, STRING


class Minion_Brand(Model):

    brandId = Field(data_type=NUMBER, hash_key=True)
    brandName = Field(data_type=STRING)
    brandCategory = Field(data_type=STRING)

    def __init__(self, brandId, brandName, brandCategory):
    	super(Minion_Brand, self).__init__()
        self.brandId = brandId
        self.brandName = brandName
        self.brandCategory = brandCategory
