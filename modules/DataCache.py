import os


class DataCache:

	def __init__(self, folder):
		self.dates = []
		self.folder = folder
	
	def getDates(self):
		self.dates = os.listdir(self.folder)
		return self.dates

