from dynamo3 import DynamoDBConnection
from flywheel import Engine

from auth.auth_main import *


connection = DynamoDBConnection.connect(region=DynamoAuth.region,host="localhost",port=8000,is_secure=False,access_key=DynamoAuth.access_key,secret_key=DynamoAuth.secret_key)
#connection = DynamoDBConnection.connect(region=DynamoAuth.region,host="localhost",port=8000,is_secure=False)
#connection = DynamoDBConnection.connect_to_host()
engine = Engine(connection)
#engine.connect_to_region('us-east-1')
#engine.connect("localhost:8000")
