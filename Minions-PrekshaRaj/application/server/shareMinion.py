"""
handles  sharing minions to another user
"""

from common.globalconst import *
from server.server_common import assert_server_comm, respond_json
from server.errorhandler import *
from database.domain import *
import time

def sharing_proc(Minion_Minion M1, Minion_User User1, Minion_User User2):
	"""
	This is the function of sharing a minion to other user
	M1: the minion which is shared
	User1: the user owns M1 before sharing
	User2: the user owns M1 after sharing
	User1 gives M1 to User2
	s1 is the instance of sharing record in database
	"""

	M1.userId = User2.userId
	sharingid = id_generator(INT_LENGTH_USER_ID)
	share_time = time.time()
	Minion_Sharing s1 = Minion_Sharing(sharingid, M2.userId, M1.userId, M1.minion_type, 1, "sharing", share_time)

	return s1

