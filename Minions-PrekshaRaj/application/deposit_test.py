from server.httpcomm.interface import *
from common.globalfunct import json_encode


TEST_URL1_LOCALHOST = '127.0.0.1:5000'


print '######################## USER SIGNUP TEST #############################'
test_body_1 = json_encode({"username": "testuser12345",
                           "password": "password12345",
                           "email": "test12345@test.com",
                           "signuptype": "regular"})
auth = {"Authorization":"prek"}
retdata = simple_http_request(TEST_URL1_LOCALHOST,
                              test_body_1, 'POST',
                              '/signup',headers=auth
                              )
print 'User information used:', test_body_1
print 'status:', retdata.status
mydata = retdata.read()
print 'body:', mydata


print '######################## LOGIN TEST ###########################'
test_body_2 = json_encode({"username": "testuser12345",
                           "password": "password12345"})
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



#print 'Test Vault Update...'
#test_body_2 = json_encode( {"coins":
#      [
#        {"brandId": 2, "coinAmt": 10},
#        {"brandId": 3, "coinAmt": 5}
#      ]
#    }
#)
#retdata = simple_http_request(TEST_URL1_LOCALHOST,
#                              test_body_2, 'POST',
#                              '/vault/update',headers={"Authorization":"prek",'userId':dat['userId'],'token': dat['secret_token']}
#                              )
#print 'status:', retdata.status
#mydata = retdata.read()
#print 'body:', mydata


print '######################## VAULT DEPOSIT TEST ######################'
test_body_2 = json_encode( {"coins":
      [
        {"brandId": 2, "coinAmt": 10},
        {"brandId": 3, "coinAmt": 20},
	{"brandId": 10, "coinAmt": 40}
      ]
    }
)
retdata = simple_http_request(TEST_URL1_LOCALHOST,
                              test_body_2, 'POST',
                              '/vault/deposit',headers={"Authorization":"prek",'userId':dat['userId'],'token': dat['secret_token']}
                              )
print 'status:', retdata.status
mydata = retdata.read()
print 'body:', mydata


print '##################### VAULT STATUS AFTER DEPOSIT #########################'
test_body_2 = json_encode({})
retdata = simple_http_request(TEST_URL1_LOCALHOST,test_body_2,'GET',
                              '/vault/status',headers={"Authorization":"prek",'userId':dat['userId'],'token': dat['secret_token']}
                              )
print 'status:', retdata.status
mydata = retdata.read()
print 'body:', mydata


print '#################### LOGOUT TEST ##############################'
print 'Test Logout...'
test_body_2 = json_encode({})
retdata = simple_http_request(TEST_URL1_LOCALHOST,test_body_2,'GET',
                              '/logout',headers={"Authorization":"prek",'userId':dat['userId'], 'token': dat['secret_token']}
                              )
print 'status:', retdata.status
mydata = retdata.read()
print 'body:', mydata


