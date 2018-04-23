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
b_k = 10

#a) Regula-Falsi:
iteraciones = 60
print "k\t\ta_k\t\tb_k\t\tF(a_k),'\t\t', F(b_k),'\t\t', m_kmas1, \t\t F(m_kmas1)"
for k in range(iteraciones):
    m_kmas1 = a_k - ((b_k - a_k) / (F(b_k) - F(a_k))) * F(a_k)
    print k,'\t\t', a_k,'\t\t', b_k,'\t\t', F(a_k),'\t\t', F(b_k),'\t\t', m_kmas1, '\t\t', F(m_kmas1)
    if (F(m_kmas1) == 0):
        raiz = m_kmas1
        print "RAIZ HALLADA: ", raiz
        break
    elif (F(m_kmas1) * F(a_k) > 0):
        a_k = m_kmas1
    else:
        b_k = m_kmas1
        
    

