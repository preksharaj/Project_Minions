from plaid import Client
from plaid import errors as plaid_errors
from plaid.utils import json
from common.globalconst import *
from server.server_common import respond_json
from server.errorhandler import *
from auth.auth_main import plaid_client_id, plaid_secret, plaid_public_key


Client.config({
    'url': 'https://tartan.plaid.com'
})
client = Client(client_id=plaid_client_id, secret=plaid_secret)


def GetInstitutions():
	institutions = client.institutions().json()
	return institutions

def GetCategories():
	categories = client.categories().json()
	return categories


def AddUser(account_type='', username='', password=''):
	"""
	Method to add new user in plaid account. if response is 200 then user is connected. 
	If response is 201, then MFA is required
	"""
	try:
	    response = client.connect(account_type, {
	     'username': username,
	     'password': password
	    })
	except plaid_errors.PlaidError, e:
		msg = {}
		msg['code'] = INT_ERROR_GENERAL
		msg['message'] = str(e)
		return msg
	else:
		if response.status_code == 200:
			data = response.json()
			return data
		elif response.status_code == 201:
			# 201 indicates that additional MFA steps required
			data = response.json()
			return data

def AddUserPatch(access_token, username, password):
	try:
		client.access_token = access_token
		response = client.connect_update({'username': username,'password': password})
	except plaid_errors.PlaidError, e:
		msg = {}
		msg['code'] = INT_ERROR_GENERAL
		msg['message'] = str(e)
		return msg
	else:
		if response.status_code == 200:
			data = response.json()
			return data
		elif response.status_code == 201:
			# 201 indicates that additional MFA steps required
			data = response.json()
			return data	


def DeleteUser(access_token):
	client.access_token = access_token
	return client.connect_delete()

def GetTransactions(access_token):
	client.access_token = access_token
	return client.connect_get()

#for list(code), we send account_type and answer (string code)
#for question, we send answers in a string form. For each answer we make a seperate request
#for selection, we create a json array with answers in the same order as questions
def answer_question(account_type, access_token, answer):
	client.access_token = access_token
	return client.connect_step(account_type, answer)


def answer_list(account_type, access_token, mfatype, mfavalue):
    #if type is mfa
    #options='{"send_method":{"type":"phone"}}'
    sendMethod = {'send_method':{ mfatype: mfavalue}}
    client.access_token = access_token
    return client.connect_step(account_type, None, options=sendMethod)




