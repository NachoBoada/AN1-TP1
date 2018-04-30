'''TP1-AN1'''
#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from __future__ import division #Para tener muchos digitos despues de la coma

    #Declaro variables del problema
NP = 99411
g = 9.81
Lo =  2 * 100000 / NP
Lo = round(Lo, 3)
K = 10
Mo = 100000 / NP
Mo = round(Mo, 3)
a = 1

#Esta es la funcion a la que se le deben hallar las raices
''' Fy = -2 * k * y * (1 - (Lo / (y**2 + a**2))**(1/2)) - m * g '''
def F(y, m = 0):
    return (-2 * K * y * (1 - (Lo / (y**2 + a**2))**(1/2)) - m * g)

    
    

''' Punto 1 - Mo = 0 '''
a_k = 0.1
b_k = 1.1

#a) Regula-Falsi:
iteraciones = 60
r_k = 0 #Lo inicializo para poder usarlo en cuando k>0, sino da error.
print "k\ta_k\tb_k\tF(a_k)\tF(b_k)\tr_kmas1\tDELTAr (r_k - r_k-1)\tDELTAr/r_k"
for k in range(iteraciones):
    r_kmas1 = a_k - ((b_k - a_k) / (F(b_k) - F(a_k))) * F(a_k)
    if k == 1:
        print "" #Para que no imprima todo junto porque cuando k=0 los delta r no existen.
    print k, '\t', a_k, '\t', b_k, '\t', F(a_k), '\t', F(b_k), '\t', r_kmas1,
    if (F(r_kmas1) == 0):
        raiz = r_kmas1
        delta_r_kmas1 = r_kmas1 - r_k
        err_rel = abs(delta_r_kmas1 / r_kmas1)
        print '\t', delta_r_kmas1, '\t', err_rel
        print "\nRAIZ HALLADA: ", raiz
        break
    elif (F(r_kmas1) * F(a_k) > 0):
        a_k = r_kmas1
    else:
        b_k = r_kmas1
    if k > 0:
        delta_r_kmas1 = r_kmas1 - r_k
        err_rel = abs(delta_r_kmas1 / r_kmas1)
        print '\t', delta_r_kmas1, '\t', err_rel
    r_k = r_kmas1
    
    lamda = 
    orden_p = 
    



    

