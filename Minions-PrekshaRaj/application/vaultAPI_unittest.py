"""
This file tests the vault APIs.

-- William Lee
-- 4/24/2016

This file tests get vault status and update vault status to
ensure that the user's coins are being updated and retrieved
correctly.

"""
import application
from database import *
from database.domain.Vault import Minion_Vault
from common.globalfunct import *
from common.globalconst import *
import unittest
import mock
import datetime

TEST_USER_ID = 'S2Z53XK05N'


class TestVault(unittest.TestCase):

  def setUp(self):
    # Set up vault test environment
    self.app = application.application.test_client()
    coins = engine.query(Minion_Vault).filter(
      userId=TEST_USER_ID).gen()
    for coin in coins:
      setattr(coin, 'coinAmt', 0)
      engine.sync(coin)
    vault = engine.query(Minion_Vault).filter(
      userId=TEST_USER_ID, brandId=0).first()
    if vault:
      setattr(vault, 'coinAmt', 10)
      engine.sync(vault)
    else:
      curr_time = datetime.datetime.now()
      new_vault = Minion_Vault(0, TEST_USER_ID, 10, curr_time)
      engine.save(new_vault)

  @mock.patch('vaultAPI.authenticate_request')
  def test_vault(self, mock_auth):
    mock_auth.return_value = INT_OK

    # Test get vault status and confirm initial vault state
    resp = self.app.get('/vault/status',
                        headers={'userId': TEST_USER_ID}).data
    coins = json_decode(resp)['coins']
    for coin in coins:
      if coin['brandId'] == 0:
        assert coin['coinAmt'] == 10
      else:
        assert coin['coinAmt'] == 0

    # Test update vault:
    req_body = json_encode({"coins": []})
    resp = self.app.post('/vault/update', data=req_body,
                         headers={'userId': TEST_USER_ID}).data
    coins = json_decode(resp)['coins']
    assert len(coins) == 0

    req_body = json_encode({
        "coins": [{"brandId": "0", "coinAmt": "-1"}]
    })
    resp = self.app.post('/vault/update', data=req_body,
                         headers={'userId': TEST_USER_ID}).data
    coins = json_decode(resp)['coins']
    assert len(coins) == 1
    assert int(coins[0]['status']) == 0

    req_body = json_encode({
        "coins": [{"brandId": "0", "coinAmt": "-100"}]
    })
    resp = self.app.post('/vault/update', data=req_body,
                         headers={'userId': TEST_USER_ID}).data
    coins = json_decode(resp)['coins']
    assert len(coins) == 1
    assert int(coins[0]['status']) == -1

    req_body = json_encode({
        "coins": [
            {"brandId": "0", "coinAmt": "-3"},
            {"brandId": "1", "coinAmt": "10"},
            {"brandId": "3", "coinAmt": "5"},
            {"brandId": "10", "coinAmt": "-10"}
        ]
    })
    correct_status = {0: 0, 1: 0, 3: 0, 10: -1}
    resp = self.app.post('/vault/update', data=req_body,
                         headers={'userId': TEST_USER_ID}).data
    coins = json_decode(resp)['coins']
    assert len(coins) == 4
    for coin in coins:
      assert correct_status[coin['brandId']] == int(coin['status'])

    # Test get vault status
    correct_value = {0: 6, 1: 10, 3: 5, 10: 0}
    resp = self.app.get('/vault/status',
                        headers={'userId': TEST_USER_ID}).data
    coins = json_decode(resp)['coins']
    for coin in coins:
      if correct_value.has_key(coin['brandId']):
        assert correct_value[coin['brandId']] == int(coin['coinAmt'])
      else:
        assert coin['coinAmt'] == 0


if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(TestVault)
  unittest.TextTestRunner(verbosity=1).run(suite)
