from server.httpcomm.interface import *
from common.globalfunct import json_encode


TEST_URL1_LOCALHOST = '127.0.0.1:5000'


print '####################### SIGNUP TEST ##################'
test_body_1 = json_encode({"username": "testuser123",
                           "password": "password123",
                           "email": "test123@test.com",
                           "signuptype": "regular"})
auth = {"Authorization":"prek"}
retdata = simple_http_request(TEST_URL1_LOCALHOST,
                              test_body_1, 'POST',
                              '/signup',headers=auth
                              )
print 'status:', retdata.status
mydata = retdata.read()
print 'body:', mydata


print '###################### LOGIN TEST ###################'
test_body_2 = json_encode({"username": "testuser123",
                           "password": "password123"})
retdata = simple_http_request(TEST_URL1_LOCALHOST,
                              test_body_2, 'POST',
                              '/login',headers=auth
                              )
print 'status:', retdata.status
mydata = retdata.read()
print 'body:', mydata
dat = json.loads(mydata) 
print 'user id is:',dat['userId']
print 'token is:', dat['secret_token']




print '#################### LOGOUT TEST #####################'
test_body_2 = json_encode({})
retdata = simple_http_request(TEST_URL1_LOCALHOST,test_body_2,'GET',
                              '/logout',headers={"Authorization":"prek",'userId':dat['userId'], 'token': dat['secret_token']}
                              )
print 'status:', retdata.status
mydata = retdata.read()
print 'body:', mydata

