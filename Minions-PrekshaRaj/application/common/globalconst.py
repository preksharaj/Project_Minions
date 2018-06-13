"""
This is the file that defines all global codes

NOTE: All stuff in flask are session-specific

NOTHING exists for a session after the session dies

- Chen

3/7/2016

"""
import re


STR_SERVER_VER = '0.1(Alpha)'

STR_SERVER_LOG_FLAG = '[KASHFLOW SERVER]'

STR_UNDEFINED = 'Undefined'
STR_NOTFOUND = 'Notfound'

STR_SUCCESS = 0

STR_ERROR_GENERAL = '-1'
STR_ERROR_DUPLICATEUSERNAME = '-2'

INT_ERROR_GENERAL = -1000
INT_ERROR_NOTEXIST = -3000
INT_ERROR_FOUND = -3001
INT_ERROR_PASSEDEXPTIME = -2000
INT_ERROR_FORMAT = -4000
INT_ERROR_TIMEOUT = -4008
INT_ERROR_MAXATTEMPTREACHED = -40080

INT_FAILURE = -1001
INT_FAILURE_AUTH = -1002

INT_ILLEGAL_HTTPMETHOD = -4001

INT_NOTEXISTS = 3000
INT_FOUND = 3001
INT_LOGGEDOUT = 1009
INT_OK = 0
INT_CREATED = 2001

TOKEN_VALIDTIME = 120  # 120 min of valid token
TOKEN_LENGTH = 30

INT_TTL_GEN_ID = 10  # no. of attempt to try generating id using id_generator(num)

INT_LENGTH_USER_ID = 10  # length of user id (by id_generator)

INT_UPDATE_FAILED = -1  # failed to update coin amount
INT_UPDATE_SUCCEEDED = 0  # succeeded in updating coin amount

FIN_IS_TESTDRIVE = True  # whether we are on test drive mode with Finicity


RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')

RE_URL = re.compile(r'^[0-9a-z\.\-\_]{1,50}$')
RE_SUBURL = re.compile(r'^[0-9a-z\\\-\_]{1,50}$')


LIST_HTTPMETHODS = {'GET', 'POST', 'HEAD', "PUT", 'DELETE'}

SIGNUP_TYPES = {'regular', 'facebook', 'twitter', 'googleplus'}
