'''TP1-AN1'''
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from __future__ import division #Para tener muchos digitos despues de la coma
import math


    #Declaro variables del problema
NP = 99411
g = 9.81
Lo =  2 * 100000 / NP
Lo = round(Lo, 3)
K = 10
Mo = 100000 / NP
Mo = round(Mo, 3)
a = 1

#Funcion a la que deseo hallar punto fijo
#Provisoria: utilizo raiz de x como ejemplo para probar que primero
#funciona el metodo implementado
def F(y):
    return math.sqrt(y)

#Proximo, se define un punto perteneciente al intervalo que cumple con los requisitos
#xseed por la variable x y por ser la semilla del problema :)
xseed = 0.5


#b) Punto Fijo:
iteraciones = 60
print "k\t\tx_k\t\tDELTAX (x_k - x_k-1)\t\tDELTAX/X_k"
x_k = xseed
for k in range(iteraciones):
    x_kmas1 = F(x_k)
    print k+1,'\t\t', x_kmas1,'\t\t', x_kmas1 - x_k,'\t\t', (x_kmas1 - x_k)/x_k
    if (x_kmas1 == x_k):
        raiz = x_kmas1
        print "RAIZ HALLADA: ", raiz
        break
    x_k = x_kmas1
