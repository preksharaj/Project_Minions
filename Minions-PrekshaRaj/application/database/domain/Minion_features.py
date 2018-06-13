from flywheel import Model, Field, Engine, NUMBER, STRING
from datetime import datetime


class Minion_Minion_features(Model):
    featureId = Field(data_type=NUMBER, range_key = True)
    minionId = Field(data_type=NUMBER, hash_key = False)
    featureType = Field(data_type=STRING)
    feature_startDate = Field(datetime)
    feature_expiry = Field(datetime)
    feature_isactive = Field(data_type=NUMBER)

    def __init__(self, featureId, minionId, featureType, feature_startDate, feature_isactive):
        super(Minion_Minion_features, self).__init__()
        self.featureId = featureId
        self.minionId = minionId
        self.featureType = featureType
        self.feature_startDate = feature_startDate
        self.feature_isactive = feature_isactive
