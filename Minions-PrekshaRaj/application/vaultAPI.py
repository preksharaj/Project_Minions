'''
This file contains APIs related to updating and retrieving user
Vault.

-- William Lee
-- 11/16/16

This file has user Vault update and retrieval methods.

'''
from flask import Blueprint, request
from server.server_common import authenticate_request, respond_json
from server.vault import GetCoins, UpdateCoins, WithdrawCoins, DepositCoins
from common.globalconst import *
from common.globalfunct import *

vault_api = Blueprint('vault_api', __name__)


@vault_api.route('/status', methods=['GET'])
def GetVault():
  """
  Gets all Vault fields.

  Returns:
    State of users vault in the following format:

      {coins: [{coin1 fields}, {coin2 fields}, ...]}

  """
  status_code = authenticate_request(request.headers, request.remote_addr)
  if status_code != INT_OK:
    return respond_json(status_code)
  user_id = request.headers['userId']
  vault = GetCoins(user_id)
  if vault is None:
    return respond_json(INT_ERROR_NOTEXIST)
  return respond_json(INT_OK, **vault)


@vault_api.route('/update', methods=['POST','GET'])
def UpdateVault():
  """
  Deposits specified coin amounts into vault
  Request body contains a 'coins' key with a list of
  dictionaries as it's value:

    {coins:
      [
        {brandId: 2, coinAmt: 10},
        {brandId: 3, coinAmt: -5}
        ...
      ]
    }

  Negative coinAmt = withdrawal
  Positive coinAmt = deposit

  Returns:
    Same format as input, except with success status for each
    coin update. For example:

      {coins:
        [
          {brandId: 2, coinAmt: 10, status: 0},
          {brandId: 3, coinAmt: -5, status: -1}
          ...
        ]
      }

    A status of 0 indicates success, and a status of -1 indicates
    failure.
  """
  status_code = authenticate_request(request.headers, request.remote_addr)
  if status_code != INT_OK:
    return respond_json(status_code)
  user_id = request.headers['userId']
  fields = json_decode(request.data)
  if fields.has_key('coins'):
    coins_result = UpdateCoins(user_id, fields['coins'])
    return respond_json(INT_OK, **coins_result)
  else:
    return respond_json(INT_ERROR_FORMAT)


@vault_api.route('/withdraw', methods=['POST','GET'])
def WithdrawVault():

  status_code = authenticate_request(request.headers, request.remote_addr)
  if status_code != INT_OK:
    return respond_json(status_code)
  user_id = request.headers['userId']
  fields = json_decode(request.data)
  if fields.has_key('coins'):
    coins_result = WithdrawCoins(user_id, fields['coins'])
    return respond_json(INT_OK, **coins_result)
  else:
    return respond_json(INT_ERROR_FORMAT)


@vault_api.route('/deposit', methods=['POST','GET'])
def DepositVault():

  status_code = authenticate_request(request.headers, request.remote_addr)
  if status_code != INT_OK:
    return respond_json(status_code)
  user_id = request.headers['userId']
  fields = json_decode(request.data)
  if fields.has_key('coins'):
    coins_result = DepositCoins(user_id, fields['coins'])
    return respond_json(INT_OK, **coins_result)
  else:
    return respond_json(INT_ERROR_FORMAT)

