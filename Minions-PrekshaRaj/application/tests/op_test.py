from server.httpcomm.interface import *
from common.globalfunct import json_encode


TEST_URL1_LOCALHOST = '127.0.0.1:5000'

"""
print 'Test Login...'
test_body_1 = json_encode({"username": "testuser",
                           "password": "password1"})
retdata = simple_http_request(TEST_URL1_LOCALHOST,
                              test_body_1, 'POST',
                              '/login'
                              )
print 'status:', retdata.status
mydata = retdata.read()
print 'body:', mydata
"""

"""
print 'Test Renew...'
test_body_2 = json_encode({"op": "renewtoken"})
retdata = simple_http_request(TEST_URL1_LOCALHOST,
                              test_body_2, 'POST',
                              '/op', False, {'userId': 'RFDX7ISX8T', 'token': 'R0XYR0GVCM9VUGDYNI0638S1GAQ9OX'}
                              )
print 'status:', retdata.status
mydata = retdata.read()
print 'body:', mydata
"""


print 'Test Logout...'
test_body_2 = json_encode({"op": "logout"})
retdata = simple_http_request(TEST_URL1_LOCALHOST,
                              test_body_2, 'POST',
                              '/op', False, {'userId': 'testuser', 'token': 'AROJH1E1C9CU4SO0MG1E9CNHOU82DY'}
                              )
print 'status:', retdata.status
mydata = retdata.read()
print 'body:', mydata

