"""
This is the test file for finicity interface
"""
from server.httpcomm.interface import *


# to test the http handler

status_code, retdata = http_request('127.0.0.1', '/')
print 'return data:\n', retdata
