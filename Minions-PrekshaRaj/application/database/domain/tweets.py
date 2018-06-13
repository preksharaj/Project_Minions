
from flywheel import Model, Field, NUMBER


class Minion_Tweets(Model):

    tweetId = Field(data_type=NUMBER, hash_key=True)
    socialId = Field(data_type=NUMBER , range_key=True)
    retweetNum = Field(data_type=NUMBER)
    favNum = Field(data_type=NUMBER)

    def __init__(self, tweetid='', socialid='',
                 retweetnum='', favnum=''):
        super(Minion_Tweets, self).__init__()
        self.tweetId = tweetid
        self.socialId = socialid
        self.retweetNum = retweetnum
        self.favNum = favnum
