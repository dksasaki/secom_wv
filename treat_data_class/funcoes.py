#######################################################
### Codigo para procurar pontos da grade proximos   ###
### a uma coordenada específica (boia, por exemplo) ###
#######################################################

import numpy as np

def procurar_pontos_grade( x , y , xm , ym , n=1):
    """
    Codigo para procurar pontos da grade proximos   
    a uma coordenada específica (boia, por exemplo) 
    x :  posição na direção 1 a ser encontrada
    y :  posição na direção 2 a ser encontrada
    xm:  matriz de posições x
    ym:  matriz de posições y
    n :  número de pontos a ser encontrado

    Ex:

    xm, ym = np.meshgrid(np.arange(10),np.arange(10))
    x = 2.2
    y = 4.5
    
    procurar_pontos_grade(x,y,xm,ym,n=2)
    """
    dist = np.full_like(xm , np.nan)
    for i in range(np.size(lon,0) ):
        for j in range(np.size(lon,1)):
            dist[i,j] =  (xm[i,j] - x)**2 + (ym[i,j] - y)**2


    res = np.argsort(dist, axis=None)

    resultado = np.zeros([n,2]) 

    for i in range( n ):
        resultado[i,0] = res[i]//np.size(dist,1) 
        resultado[i,1] = res[i]%np.size(dist,1) 

    return resultado
