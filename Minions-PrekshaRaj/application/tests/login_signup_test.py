from server.httpcomm.interface import *
from common.globalfunct import json_encode


TEST_URL1_LOCALHOST = '127.0.0.1:80'


print 'Test Signup...'
test_body_1 = json_encode({"username": "test_userkk",
                           "password": "password221",
                           "email": "test2@test.com",
                           "signuptype": "regular"})
retdata = simple_http_request(TEST_URL1_LOCALHOST,
                              test_body_1, 'POST',
                              '/signup'
                              )
print 'status:', retdata.status
mydata = retdata.read()
print 'body:', mydata


print 'Test Login...'
test_body_2 = json_encode({"username": "testuser",
                           "password": "password1"})
retdata = simple_http_request(TEST_URL1_LOCALHOST,
                              test_body_2, 'POST',
                              '/login'
                              )
print 'status:', retdata.status
mydata = retdata.read()
print 'body:', mydata
