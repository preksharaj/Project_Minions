"""
This is the interface py file for database for user management
"""
from database import *
from database.domain.user import Minion_User
from common.globalconst import *
from server.errorhandler import InvalidUsage
from common.globalfunct import id_generator

import time, datetime


def create_new(username=None, password=None,
               email=None, signuptype=None):
    """
    :param username:
    :param password:
    :param email:
    :param signuptype:
    :return: status code of this creation
    """
    try:
        assert username
        assert password
        assert email
        assert signuptype
    except AssertionError:
        raise InvalidUsage('Wrong parameters for creating new user. Expecting username, password, email, signup', 400)
    status_code, tmp_obj = _find_user(username, email)
    if status_code == INT_FOUND:
        return INT_ERROR_FOUND
    elif status_code == INT_NOTEXISTS:
        success_signal = False
        ttl = INT_TTL_GEN_ID
        userid = id_generator(INT_LENGTH_USER_ID)
        while success_signal is False and ttl > 0:
            tokenquery = engine.query(Minion_User).filter(userId=userid).all()
            if len(tokenquery) == 0:  # success in gen random userid
                user = Minion_User(userid, username, password, email)
                user.signuptype = signuptype
                user.date_signup = datetime.datetime.now()
                engine.save(user)
                success_signal = True
            else:
                userid = id_generator(INT_LENGTH_USER_ID)
            ttl -= 1
        if success_signal is True:
            return INT_CREATED
        else:
            return INT_ERROR_MAXATTEMPTREACHED


def security_check(userid='', token='', client_ip='', force_invalidate=False):
    """
    This is mainly for every time op security check
    on:
        wrong secret
        stale secret
        different client ip
    we invalidate the current token and ask for a new login
    :param userid:
    :param token:
    :param force_invalidate:
    :param client_ip:
    :return:
    """
    if userid == '' or token == '' or client_ip == '':
        return INT_ERROR_FORMAT
    try:
        my_user = engine.query(Minion_User).filter(userId=userid).first()
        if my_user:
            if isinstance(my_user, Minion_User):
                remote_ip = str(my_user.client_ip)
                if remote_ip.strip() == client_ip:
                    remote_token = str(my_user.secret_token)
                    if remote_token.strip() == token:
                        current_time = time.time()
                        if my_user.secret_token_exp > current_time - TOKEN_VALIDTIME:
                            if force_invalidate:
                                invalidate_secret(my_user)
                            return INT_OK
                        else:
                            return INT_ERROR_PASSEDEXPTIME
                # if auth failed, remove the token, exp, and client_ip stored
                # meaning requiring the client to log in again
        return INT_FAILURE_AUTH
    except all as e:
        print 'Error in security_check:', e
        raise


def invalidate_secret(my_user=None):
    try:
        assert engine
        assert my_user
        assert isinstance(my_user, Minion_User)
    except AssertionError:
        print 'Error in invalidate_secret'
        raise
    my_user.secret_token = ' '
    my_user.secret_token_exp = 0
    my_user.client_ip = ' '
    try:
        my_user.sync()
    except all as e:
        print 'Error in invalidating secret:', e
        raise


def renew_token(userid='', client_ip=''):
    try:
        assert userid != ''
        assert client_ip != ''
    except AssertionError:
        print 'Error in renew_token'
        raise
    current_user = _get_user(userid)
    try:
        assert current_user
    except AssertionError:
        print 'Error in renew_token'
        raise
    status_code, userid, mytoken, mytoken_valid_time = _generate_token(current_user, client_ip)
    return status_code, userid, mytoken, mytoken_valid_time


def verify_user(username='', password='', token=False, client_ip=''):
    """
    This is mainly for log in
    :param username:
    :param password:
    :param token:
    :param client_ip:
    :return: status code of this verification
    """
    try:
        assert username != ''
        assert password != ''
        assert client_ip != ''
    except AssertionError:
        print 'error in passing parameters in verify_user'
        if token:
            return INT_FAILURE, None, None, None
        else:
            return INT_FAILURE, None
    try:
        my_user = engine.scan(Minion_User).\
                       filter(userName=username).all()
        if len(my_user) == 0:
            if token:
                return INT_ERROR_NOTEXIST, None, None, None
            else:
                return INT_ERROR_NOTEXIST, None
        current_user = my_user[0]
        assert current_user
        assert isinstance(current_user, Minion_User)
        if current_user.userId != '':
            if current_user.password == password:
                assert current_user.userId
                # start of the success area:
                if token is False:
                    return INT_OK, current_user.userId  # meaning not found
                else:
                    # generating token and valid_time
                    status_code, userid, mytoken, mytoken_valid_time = _generate_token(current_user, client_ip)
                    return status_code, userid, mytoken, mytoken_valid_time
            else:
                if token:
                    return INT_FAILURE_AUTH, None, None, None
                else:
                    return INT_FAILURE_AUTH, None
        if token:
            return INT_ERROR_GENERAL, None, None, None
        else:
            return INT_ERROR_GENERAL, None
    except AssertionError:
        print 'Error in verify user'
        raise



def get_user_details(userid=''):
    '''Method to get user details'''
    user = _get_user(userid)
    user = user.__dict__
    userRet = {}
    for val in Minion_User.user_attr:
        if(user.has_key(val) and user[val] is not None):
            userRet[val] = user[val]
    return userRet

def save_user_details(userid='', userdetails={}):
    user = _get_user(userid)
    for key, value in userdetails.items():
        if(value is not None):
            setattr(user, key, value)
    user.sync()


"""
private functions
"""


def _generate_token(current_user=None, client_ip=''):
    try:
        assert current_user
        assert isinstance(current_user, Minion_User)
        assert client_ip != ''
    except AssertionError:
        print 'Error in generate token'
        raise
    mytoken = id_generator(TOKEN_LENGTH)
    mytoken_valid_time = TOKEN_VALIDTIME
    mytoken_exp = int(time.time() + mytoken_valid_time * 60)
    current_user.secret_token = mytoken
    current_user.secret_token_exp = int(mytoken_exp)
    current_user.client_ip = client_ip
    current_user.sync()
    return INT_OK, current_user.userId, mytoken, mytoken_valid_time


def _find_user(username='', email=''):
    """
    This is to check if a username or email exists in dynamoDB
    :param username:
    :param email:
    :return:
    """
    try:
        result = engine.scan(Minion_User).filter(userName=username).all()
    except all as e:
        print 'Error:', e
        raise
    if len(result) > 0:
        # meaning this username already taken
        # print 'username already taken'
        """
        if email != '':
            # if we have email query, too.
            result = engine.scan(Minion_User).filter(email=email).first()
            if len(result) > 0:
                return INT_FOUND, result[0]
            else:
                return INT_NOTEXISTS, None
        """
        return INT_FOUND, result[0]
    else:
        return INT_NOTEXISTS, None
        # NOTE: it might have multiple elements in results, but there means error in db, username not unique!
"""
except all:
    print 'error in checking dup user'
    return INT_ERROR_GENERAL, None
"""


def _get_user(userid=''):
    return engine.query(Minion_User).\
                       filter(userId=userid).first()

