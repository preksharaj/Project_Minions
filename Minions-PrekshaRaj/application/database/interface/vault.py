'''
This file contains methods related to Vault state

-- William Lee
-- 11/14/2016

This file has Vault state update and retrieval methods.

'''
from common.globalconst import *
from database import *
from database.domain.Vault import Minion_Vault
import datetime


def GetVault(user_id):
  """
  Gets all coins in a users vault from database.

  Args:
    user_id: id of the user whose vault is being retrieved

  Returns:
    A dictionary with all of a users vault coins in the following
    format:

      {coins: [{coin1 fields}, {coin2 fields}, ...]}

  """
  vault_info = {'coins': []}
  coins = engine.query(Minion_Vault).filter(userId=user_id).gen()
  for coin in coins:
    vault_info['coins'].append(
      {k: v for k, v in coin.__dict__.items()
       if not k.startswith('__') and not k == 'userId'
       and not callable(k)})
  return vault_info


def UpdateCoin(user_id, brand_id, coin_change_amt):
  """
  Update a specific coin amount in the database.

  Args:
    user_id: User whose coin we want to update
    brand_id: Brand id of coin to change
    coin_change_amt: Amount to change coin by (can be + or -)

  Returns:
    An update success (0) or failure (-1) status code.  Fails
    when the user doesn't have enough coins to meet a
    withdrawal amount.
  """
  vault = engine.query(Minion_Vault).filter(
    userId=user_id, brandId=brand_id).first()
  if vault:
    existing_coins = getattr(vault, 'coinAmt')
    final_amt = existing_coins + coin_change_amt
    if final_amt < 0:
      return INT_UPDATE_FAILED
    elif final_amt > 100:
      return INT_UPDATE_FAILED
    else:
      setattr(vault, 'coinAmt', final_amt)
      engine.sync(vault)
      return INT_UPDATE_SUCCEEDED
  if coin_change_amt < 0:
    return INT_UPDATE_FAILED
  signup_time = datetime.datetime.now()
  new_vault = Minion_Vault(brand_id, user_id, coin_change_amt, signup_time)
  engine.save(new_vault)
  return INT_UPDATE_SUCCEEDED
