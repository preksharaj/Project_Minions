"""
This file has all APIs related to financial and banking transactions

-- Tushar
-- 4/30/2016

This file has Plaid connectivity methods
"""

from flask import Blueprint, request
from server.server_common import authenticate_request, respond_json
from server.banking import GetInstitutions, GetCategories, AddUser, DeleteUser, GetTransactions,\
answer_list, answer_question, AddUserPatch
from common.globalconst import *
from common.globalfunct import *

banking_api = Blueprint('banking_api', __name__)

@banking_api.route('/getbanks', methods=['GET'])
def get_banks():
	banks = GetInstitutions()
	return respond_json(INT_OK, banks=banks)



@banking_api.route('/getcategories', methods=['GET'])
def get_categories():
	cats = GetCategories()
	return respond_json(INT_OK, categories=cats)


@banking_api.route('/adduser', methods=['POST'])
def add_user():
	status_code = authenticate_request(request.headers, request.remote_addr)
	if(status_code != INT_OK):
		return respond_json(status_code)
	#check if available fields are present
	fields = json_decode(request.data)
	if fields.has_key('account') and fields.has_key('username') and fields.has_key('password'):
		#try to add user
		resp = AddUser(fields['account'], fields['username'], fields['password'])
		return respond_json(INT_OK, **resp)
	else:
		return respond_json(INT_ERROR_FORMAT)


@banking_api.route('/adduser', methods=['PATCH'])
def add_user_patch():
	status_code = authenticate_request(request.headers, request.remote_addr)
	if(status_code != INT_OK):
		return respond_json(status_code)
	#check if available fields are present
	fields = json_decode(request.data)
	#TODO: save access token in social table. Use userid to get token and update user
	if fields.has_key('access_token') and fields.has_key('username') and fields.has_key('password'):
		#try to add user
		resp = AddUserPatch(fields['access_token'], fields['username'], fields['password'])
		return respond_json(INT_OK, **resp)
	else:
		return respond_json(INT_ERROR_FORMAT)


@banking_api.route('/deleteuser', methods=['POST'])
def delete_user():
	status_code = authenticate_request(request.headers, request.remote_addr)
	if(status_code != INT_OK):
		return respond_json(status_code)
	fields = json_decode(request.data)
	#TODO: save access token in social table. Use userid to get token and delete user
	if fields.has_key('access_token'):
		try:
			resp = DeleteUser(fields['access_token'])
		except Exception, e:
			return respond_json(INT_ERROR_GENERAL, message=str(e))
		else:
			return respond_json(INT_OK)
	else:
		return respond_json(INT_ERROR_FORMAT)


@banking_api.route('/transactions', methods=['POST'])
def get_transactions():
	status_code = authenticate_request(request.headers, request.remote_addr)
	if(status_code != INT_OK):
		return respond_json(status_code)
	fields = json_decode(request.data)
	#TODO: save access token in social table. Use userid to get token and retrieve details
	if fields.has_key('access_token'):
		try:
			resp = GetTransactions(fields['access_token'])
		except Exception, e:
			return respond_json(INT_ERROR_GENERAL, msg=str(e))
		else:
			return respond_json(INT_OK, **resp.json())
	else:
		return respond_json(INT_ERROR_FORMAT)


@banking_api.route('/step/list', methods=['POST'])
def select_list_item():
	status_code = authenticate_request(request.headers, request.remote_addr)
	if(status_code != INT_OK):
		return respond_json(status_code)
	fields = json_decode(request.data)
	#TODO: save access token in social table. Use userid to get token and retrieve details
	if fields.has_key('access_token') and fields.has_key('account') and fields.has_key('mfatype') \
	and fields.has_key('mfavalue'):
		try:
			resp = answer_list(fields['account'], fields['access_token'], fields['mfatype'], fields['mfavalue'])
		except Exception, e:
			return respond_json(INT_ERROR_GENERAL, message=str(e))
		else:
			return respond_json(INT_OK)
	else:
		return respond_json(INT_ERROR_FORMAT)

@banking_api.route('/step/answer', methods=['POST'])
def send_answer():
	status_code = authenticate_request(request.headers, request.remote_addr)
	if(status_code != INT_OK):
		return respond_json(status_code)
	fields = json_decode(request.data)
	#TODO: save access token in social table. Use userid to get token and retrieve details
	if fields.has_key('access_token') and fields.has_key('account') and fields.has_key('answer'):
		try:
			resp = answer_question(fields['account'], fields['access_token'], fields['answer'])
		except Exception, e:
			return respond_json(INT_ERROR_GENERAL, message=str(e))
		else:
			return respond_json(INT_OK)
	else:
		return respond_json(INT_ERROR_FORMAT)
