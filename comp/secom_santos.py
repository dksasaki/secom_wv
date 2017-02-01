#########################################################
### PEGAR VALORES DO MODELO PRÓXIMOS À BOIA DE SANTOS ###
#########################################################
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

a = xr.open_dataset('gcmplt.cdf') #saída do secom

tempo = a['time'].data

lon = a['lon'].data#[a['lon'] == 0]
lat = a['lat'].data#[a['lat'] == 0]

lon[lon==0] = np.nan
lat[lat==0] = np.nan

variavel = { 'wh': ('Altura significativa (m)'),
			 'wd': ('Direcao da onda (graus)'),
			 'wp': ('Periodo da onda (s)') }

#escolhe a variável que vai importar
varkey = 'wd'

#Esses seis pontos da grade próximos ao pnboia Santos
var = [ a[varkey].data[: ,30,75] 
, a[varkey].data[: ,31,75]
, a[varkey].data[: ,31,76]
, a[varkey].data[: ,32,75]
, a[varkey].data[: ,32,76]
, a[varkey].data[: ,33,76] ]

# Faz a média dos 6 pontos
media = np.average(var , axis=0)



plt.plot(tempo, var[0], label='ponto 1')
plt.plot(tempo, var[1], label='ponto 2')
plt.plot(tempo, var[2], label='ponto 3')
plt.plot(tempo, var[3], label='ponto 4')
plt.plot(tempo, var[4], label='ponto 5')
plt.plot(tempo, var[5], label='ponto 6')
plt.plot(tempo, media , 'r.' , label='media', markersize='10')

plt.xlabel('Tempo')
plt.ylabel(variavel[varkey])

plt.legend()

plt.show()


