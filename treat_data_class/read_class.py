import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

class Pnboia_read(object):
	def __init__(self,name):
		self.pnboia = pd.read_csv(name)

	def get_attributes_from_data(self):
		for key in self.pnboia.keys():
				setattr(self,key,self.pnboia[key])

	def remove_repeated(self,var):
		varb = list(set(zip(self.dt,var)))
		varb.sort()
		return varb

	def datetime(self,year='yyyy',month=' mm',day=' dd',hour=' hour',minu=' min'):
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
	pn = Pnboia_read(file)
	pn.get_attributes_from_data()
	pn.datetime()