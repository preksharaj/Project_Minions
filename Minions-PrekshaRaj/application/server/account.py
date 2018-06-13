"""
handles signup
"""
from common.globalconst import *
from server.server_common import respond_json
from server.errorhandler import InvalidUsage
from database.interface.user import create_new, verify_user, get_user_details, save_user_details, \
renew_token, security_check


def signup_proc(fields=None, client_ip=STR_UNDEFINED):
    """
    This is the main proc for signup
    Protocol: signup fields:
        username
        password
        email
        signuptype:
            regular
            facebook
            twitter
            googleplus
    :param fields:
    :param client_ip:
    :return:
    """
    _signup_parsing_fields(fields)
    status_code = create_new(fields['username'],
                             fields['password'],
                             fields['email'],
                             fields['signuptype'])
    return respond_json(status_code)



def login_proc(fields=None, client_ip=STR_UNDEFINED):
    """
    This is the function that log in
    :param fields:
    :param client_ip:
    :return: on success, expect a secret token and a valid time (in min) returned
    """
    _login_parsing_fields(fields)
    status_code, userid, secret_token, secret_token_exp = verify_user((fields['username']),
                                                                      (fields['password']),
                                                                      True,
                                                                      client_ip)
    if status_code == INT_OK:
        return respond_json(INT_OK,
                            userId=userid,
                            secret_token=secret_token,
                            secret_token_exp=secret_token_exp)
    else:
        return respond_json(status_code)


def logout_proc(userid, token, client_ip):
    """
    Method to log out and set the token as expired
    """
    return respond_json(security_check(userid, token, client_ip, True))


def renew_token_proc(userid, client_ip):
    """
    Method to renew token
    """
    status_code, userid, mytoken, mytoken_valid_time = renew_token(userid, client_ip)
    if status_code == INT_OK:
        return respond_json(INT_OK,
            userId=userid,
            secret_token=mytoken,
            secret_token_exp=mytoken_valid_time)
    return respond_json(INT_ERROR_FORMAT)


def get_user_details_proc(userId):
    return get_user_details(userId)


def save_user_details_proc(userid='', fields={}):
    save_user_details(userid, fields)
    return respond_json(INT_OK)
    

"""
Private Functions
"""


def _signup_parsing_fields(fields):
    try:
        assert 'username' in fields
        assert 'password' in fields
        assert 'email' in fields
        assert 'signuptype' in fields
    except AssertionError:
        print 'Error: signup format wrong'
        raise InvalidUsage('Wrong fields format', status_code=400)
    try:
        assert RE_EMAIL.match(fields['email'])
    except AssertionError:
        print 'Error: signup email format wrong'
        raise InvalidUsage('Wrong signup email format', status_code=400)
    try:
        assert fields['signuptype'] in SIGNUP_TYPES
    except AssertionError:
        print 'Error: signup type format wrong'
        raise InvalidUsage('Wrong signup type format', status_code=400)


def _login_parsing_fields(fields):
    try:
        assert 'username' in fields
        assert 'password' in fields
    except AssertionError:
        print 'Error: login format wrong'
        raise InvalidUsage('Wrong fields format', status_code=400)
