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

#Funcion a la que deseo hallar raiz
#Provisoria: utilizo raiz de x como ejemplo para probar que primero
#funciona el metodo implementado
def F(y,m=(0.6*Mo)):
    return (2*K*y*(1-(Lo/math.sqrt((y**2)+(a**2))))-(m*g))

#Derivada de la funcion que deseo hallar raiz
def Fprima(y):
    return ((-2*K*(1-(Lo/((y**2)+(a**2))**(1/2))))+(Lo*(-0.5*((((y**2)+(a**2))**(1/2))**(-3)))*2*K*y))

#Newton Raphson es un metodo de punto fijo con una funcion de punto fijo particular
#La funcion es g(y)

def G(y):
    return (y - (F(y)/Fprima(y)))
            
#Próximo, se define un punto perteneciente al intervalo que cumple con los requisitos
#xseed por la variable x y por ser la semilla del problema :)
xseed = -3

TOPE = 4

iteraciones = 60
print "m = 0.6Mo"
while (xseed < TOPE):
    print "semilla: "
    print xseed
    print "k\t\tx_k\t\tDELTAX (x_k - x_k-1)\t\tDELTAX/X_k"
    x_k = xseed
    for k in range(iteraciones):
        x_kmas1 = G(x_k)
        print k+1,'\t\t', x_kmas1,'\t\t', x_kmas1 - x_k,'\t\t', (x_kmas1 - x_k)/x_k
        if (x_kmas1 == x_k):
            raiz = x_kmas1
            print "RAIZ HALLADA: ", raiz
            break
        x_k = x_kmas1
    xseed = xseed + 0.3
