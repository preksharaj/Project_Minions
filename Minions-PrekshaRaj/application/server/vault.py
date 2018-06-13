'''
This file contains methods related to updating and retrieving user
Vaults.

-- William Lee
-- 11/14/2016

This file has user Vault update and retrieval methods.

'''
from database.interface.vault import GetVault, UpdateCoin


def GetCoins(user_id):
  """
  Gets vault state

  Args:
    user_id: Id of user whose Vault is being retrieved

  Returns:
    A dictionary with all of a users vault coins in the following
    format:

      {coins: [{coin1 fields}, {coin2 fields}, ...]}

  """
  return GetVault(user_id)


def UpdateCoins(user_id, coins):
  """
  Update coin(s) in a user's vault.

  Args:
    user_id: Id of user whose Vault is being updated
    coins: List of coins to update.  The format is as follows:

      [
        {brandId: 5, coinAmt: 10},
        {brandId: 8, coinAmt: -5},
        ...
      ]

      A negative amount subtracts from the user's coins, and
      a positive amount adds to it.

  Returns:
    A list in same format as input, except each list entry
    now also includes the status of that update.  A status of
    0 indicates success, and a status of -1 indicates failure.
    For example:
      [
        {brandId: 5, coinAmt: 10, status: 0},
        {brandId: 8, coinAmt: -5, status: -1}
        ...
      ]
  """
  coins_result = {'coins': []}
  for coin in coins:
    coin_change_amt = int(coin['coinAmt'])
    brand_id = int(coin['brandId'])
    coin['brandId'] = brand_id
    coin['status'] = UpdateCoin(user_id, brand_id, coin_change_amt)
    coins_result['coins'].append(coin)
  return coins_result


def WithdrawCoins(user_id, coins):

  coins_result = {'coins': []}
  for coin in coins:
    coin_change_amt = int(coin['coinAmt'])
    if coin_change_amt>0:
	coin_change_amt = -(coin_change_amt)
    brand_id = int(coin['brandId'])
    coin['brandId'] = brand_id
    coin['status'] = UpdateCoin(user_id, brand_id, coin_change_amt)
    coins_result['coins'].append(coin)
  return coins_result


def DepositCoins(user_id, coins):

  coins_result = {'coins': []}
  for coin in coins:
    coin_change_amt = int(coin['coinAmt'])
    if coin_change_amt<0:
        coin_change_amt = abs(coin_change_amt)
    brand_id = int(coin['brandId'])
    coin['brandId'] = brand_id
    coin['status'] = UpdateCoin(user_id, brand_id, coin_change_amt)
    coins_result['coins'].append(coin)
  return coins_result

