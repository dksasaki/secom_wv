import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from xarray import open_dataset
from datetime import datetime

class Pnboia_read(object):
	def __init__(self):
		"""
		Reads and give a basic treatment to Pnboia dataset
		self.read_csv : read a Pnboia csv  (it uses pandas)
		self.read_csv : read a netcdf file (it uses xarray)
		"""

		self.read_csv = read_csv
		self.open_dataset = open_dataset
		self.pnboia   = None


	def get_attributes_from_data(self):
		"""
		get every key form dataset and return as a class attribute
		"""
		for key in self.pnboia.keys():
				setattr(self,key,self.pnboia[key])

	def remove_repeated(self,var):
		"""
		remove the repeated dates from the combined lists of self.dt and var
		self.dt attribute is defined by self.datetime method
		"""
		varb = list(set(zip(self.dt,var)))
		varb.sort()
		return varb

	def datetime(self,year='yyyy',month=' mm',day=' dd',hour=' hour',minu=' min'):
		"""
		create a date list using the time keys of the file
		"""
		y = self.pnboia[year]
		m = self.pnboia[month]
		d = self.pnboia[day]
		h = self.pnboia[hour]
		mi= self.pnboia[minu]

		self.dt = []
		for i in zip(y,m,d,h,mi):
			dt = '%04d-%02d-%02d %02d:%02d:00' % (i[0],i[1],i[2],i[3],i[4])
			self.dt.append(datetime.strptime(dt, '%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
	file ='file'
	pn = Pnboia_read()
	pn.read_csv(file)
	pn.get_attributes_from_data()
	pn.datetime()