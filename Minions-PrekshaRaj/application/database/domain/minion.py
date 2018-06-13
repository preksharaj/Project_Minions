from datetime import datetime

from flywheel.fields.types import DateTimeType

from flywheel import Model, Field, NUMBER, STRING, set_


class Minion_Minion(Model):

    minionId = Field(data_type=NUMBER, hash_key=True)
    userId = Field(data_type=STRING, range_key=True)
    brandId = Field(data_type=NUMBER)
    minion_name = Field(data_type=STRING)
    minion_type = Field(data_type=STRING)
    minion_dob = Field(data_type=datetime)
    minion_mood = Field(data_type=NUMBER)
    minion_health = Field(data_type=NUMBER)
    minion_state = Field(data_type=NUMBER)

    def __init__(self, minionId, userId, brandId, minion_name, minion_type, minion_dob):
        super(Minion_Minion, self).__init__()
        self.minionId = minionId
        self.userId = userId
        self.brandId = brandId
        self.minion_name = minion_name
        self.minion_type = minion_type
        self.minion_dob = minion_dob
