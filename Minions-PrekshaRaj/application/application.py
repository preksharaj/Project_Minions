"""
This is the main gateway of projMinion backend

-- Chen
-- 4/14/2016

This file has User Registration, Login, Get/Update user detail methods
"""
from flask import Flask, request
from server.errorhandler import *
from auth.auth_main import application_secret_key
from common.globalconst import *
from common.globalfunct import *
from server.account import signup_proc, login_proc, get_user_details_proc, save_user_details_proc, \
renew_token_proc, logout_proc
from server.server_common import authenticate_request, respond_json

#api imports
from bankingAPI import banking_api
from vaultAPI import vault_api

#registering other files with the main file
application = Flask(__name__)
application.register_blueprint(banking_api, url_prefix='/banking')
application.register_blueprint(vault_api, url_prefix='/vault')


@application.route('/')
def app_demo():
    """
    This is the simple demo
    :return:
    """
    return 'This is a simple demo for projminion<br>'+request.remote_addr+':8000' \
           'for any mobile-end operations data is '+request.data+'<br>' \
           'please use "/signup" to signup<br>' \
           '"/login" to login<br>' \
           '"/logout" to logout<br>' \
           '"/op" to process any operations<br>' \
           'Please follow the specific opcode instructions.'


@application.route('/signup', methods=['GET','POST'])
def app_signup():
    """
    App to sign up a new user
    :return:
    """
    signup_fields = json_decode(request.data)
    #return "sign up page"+request.data
    return signup_proc(signup_fields, request.remote_addr)


@application.route('/login', methods=['GET','POST'])
def app_login():
    """
    API to login and generate a token
    :return:
    """
    login_fields = json_decode(request.data)
    return login_proc(login_fields, request.remote_addr)


@application.route('/logout', methods=['GET'])
def app_logout():
    """
    API to log the user out. this will set the token as expired.
    :return:
    """
    status_code = authenticate_request(request.headers, request.remote_addr)
    if(status_code != INT_OK):
        return respond_json(status_code)
    return logout_proc(request.headers['userId'], request.headers['token'], request.remote_addr)


@application.route('/renewtoken', methods=['GET'])
def renewtoken():
    status_code = authenticate_request(request.headers, request.remote_addr)
    if(status_code != INT_OK):
        return respond_json(status_code)
    return renew_token_proc(request.headers['userId'], request.remote_addr)

@application.route('/user', methods=['GET'])
def user_get():
    """
    API to fetch user details
    """
    status_code = authenticate_request(request.headers, request.remote_addr)
    if(status_code != INT_OK):
        return respond_json(status_code)
    userid = request.headers['userId']
    user = get_user_details_proc(userid)
    return respond_json(INT_OK, **user)

@application.route('/user', methods=['POST'])
def user_post():
    """
    Method to save/update user details
    """
    status_code = authenticate_request(request.headers, request.remote_addr)
    if(status_code != INT_OK):
        return respond_json(status_code)
    userid = request.headers['userId']
    save_user_details_proc(userid, json_decode(request.data))
    return respond_json(INT_OK)

@application.errorhandler(404)
def page_not_found(error):
    """
    This is to process error http requests
    :param error:
    :return:
    """
    print '404 error, redirecting...'
    return '404 error, redirecting...'


@application.errorhandler(500)
def page_not_found(error):
    """
    This is to process error http requests
    :param error:
    :return:
    """
    print '500 Error. Server Internal Error...'
    return '500 Error. Server Internal Error...'


@application.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = json_encode_flask(error.to_dict())
    response.status_code = error.status_code
    return response


# starter
if __name__ == '__main__':
    application.secret_key = application_secret_key
    application.debug = True
    #application.run(host='0.0.0.0', port=80)
    application.run(debug=True);
