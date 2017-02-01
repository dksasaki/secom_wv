import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


class Filters(object):
	def __init__(self,n=11,fill_value=-99999):
		self.n = n
		self.fill_value = fill_value

	def filter_median_data(self,var):
		if self.n % 2 == 1:
			varb = []
			n1   = self.n/2
			n2   = self.n/2+1
			for i in range(n1,np.size(var)-n2):
				varb.append(np.nanmedian(var[i-n1:i+n2]))
			return varb
		else:
			print 'n must be even'

	def substitute_for_nan_values(self,var):
		varb           = np.array(var)
		varb[varb==self.fill_value] = np.nan
		return varb

	def cut_interval_by_index(self,var):
		n1   = self.n
		n2   = self.n+1

		varb = var[n1:-n2]
		return varb

if __name__ == '__main__':
	from pydap.client import open_url
	import matplotlib.pyplot as pl
	import xarray as xr
	buoy = xr.open_dataset('http://opendap.saltambiental.com.br:8080/pnboia/Bsantos.nc')

	f  = Filters()
	v  = buoy['wave_hs'].data
	v1 = f.substitute_for_nan_values(v)
	v2 = f.filter_median_data(v1)
	d  = f.cut_interval_by_index(buoy['time'])

	plt.figure()
	plt.plot(d,v2)
