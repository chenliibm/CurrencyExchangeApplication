from modules.DataCache import *


def testGetDate():
	DC = DataCache('./data')
	dates = DC.getDates()
	assert isinstance(dates, list)



