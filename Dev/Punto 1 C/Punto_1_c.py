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
#Provisoria: utilizo raiz de y como ejemplo para probar que primero
#funciona el metodo implementado
def F(y,m=0):
    return (-2*K*y*(1-Lo/(math.sqrt((y**2)+(a**2))))-m*g)

#Derivada de la funcion que deseo hallar raiz
def Fprima(y):
    return (-2*K*(1-Lo*((y**2+a**2)**(-1/2)))-2*K*y*(Lo*y*((y**2+a**2)**(-3/2))))

#Newton Raphson es un metodo de punto fijo con una funcion de punto fijo particular
#La funcion es g(y)

def G(y):
    return (y - (F(y)/Fprima(y)))

def cte_asintotica_del_error(y_kmas1, y_k, y_kmenos1, p):
    return (abs((y_kmas1 - y_k)) / abs((y_k - y_kmenos1))**p)

def orden_de_convergencia(y_kmas1, y_k, y_kmenos1, y_kmenos2):
    return (math.log( abs((y_kmas1 - y_k))/ abs((y_k - y_kmenos1)) ) / math.log( abs((y_k - y_kmenos1))/ abs((y_kmenos1 - y_kmenos2)) ))

            
#Proximo, se define un punto perteneciente al intervalo que cumple con los requisitos
#yseed por la variable y y por ser la semilla del problema :)
yseed = 3


#c) Newton-Raphson:
iteraciones = 60
y_kmenos2 = 0
y_kmenos1 = 0
#print "k\t\ty_k\t\tDELTAy (y_k - y_k-1)\t\tDELTAy/y_k"
print "k\ty_k\tDELTAy\tDELTAy/y_k\tlambda\tp"
print 0, "\t", yseed
y_k = yseed
for k in range(iteraciones):
    y_kmas1 = G(y_k)
    print k+1,'\t', y_kmas1,'\t', abs(y_kmas1 - y_k),'\t', abs(y_kmas1 - y_k)/y_k,
    if k > 2: #Necesito 4 valores de y
        p = orden_de_convergencia(y_kmas1, y_k, y_kmenos1, y_kmenos2)
        lamda = cte_asintotica_del_error(y_kmas1, y_k, y_kmenos1, p)
        print '\t', lamda, '\t', p,
    if (F(y_kmas1) == 0): # if(y_kmas1== y_k):
        raiz = y_kmas1
        print "\nRAIZ HALLADA: ", raiz
        break
    print ""
    y_kmenos2 = y_kmenos1
    y_kmenos1 = y_k
    y_k = y_kmas1
