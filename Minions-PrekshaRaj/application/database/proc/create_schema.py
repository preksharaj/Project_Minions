from dynamo3 import DynamoDBConnection
from flywheel import Engine

from auth.auth_main import *

from database import *

from database.domain.brand import Minion_Brand
from database.domain.Coins_received import Minion_Coins_received
from database.domain.Coins_spent import Minion_Coins_spent
from database.domain.minion import Minion_Minion
from database.domain.Minion_features import Minion_Minion_features
from database.domain.Sharing import Minion_Sharing
from database.domain.Shop import Minion_Shop
from database.domain.Social import Minion_Social
from database.domain.Transaction import Minion_Transaction
from database.domain.tweets import Minion_Tweets
from database.domain.user import Minion_User
from database.domain.Vault import Minion_Vault



'''
Connects to localhost:8000 by default
Refer to http://pynamodb.readthedocs.org/en/latest/local.html for how to install dynamoDb locally
Change it to the aws server when ready
For the orm api, refer to http://flywheel.readthedocs.org/en/latest/topics/getting_started.html
'''
# connection = DynamoDBConnection.connect(region="us-west-2", host="localhost", port=8000, is_secure=False)
# connection = DynamoDBConnection.connect_to_host()
# for model in [User, UserAccount, Institution, CreditCardOffer, CreditCardAccount, Benefit, BankAccount]:
# 	print(model.meta_)

engine.register(Minion_Brand, Minion_Coins_received, Minion_Coins_spent, Minion_Minion, Minion_Minion_features, Minion_Sharing, \
	Minion_Shop, Minion_Social, Minion_Transaction, Minion_Tweets, Minion_User, Minion_Vault)
engine.create_schema()
