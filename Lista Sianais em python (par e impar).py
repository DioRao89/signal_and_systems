# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:30:57 2020

@author: Cliente
"""

from numpy import linspace, zeros
import matplotlib.pyplot as plt 
pontos = 1000
inf = -4
sup = 4
vet = linspace(inf,sup,pontos)
x = zeros(pontos)
# indice i vai de zero a 999
# vetor do eixo horizontal t vai de -2 a 2
a,b,c = -1,0,1
for i,t in enumerate(vet):
    if t>=a and t<b:
        x[i] = 1
    if t>=b and t<c:
        x[i] = 1-t
 
plt.plot(vet,x)
plt.show()

#a)

a,b,c = -1,0,1

for i,t in enumerate(vet):
    x[i] = 0.5*x[i]
 
plt.plot(vet,x)
plt.show()

#2) sinal par 
#criando um vetor com mil zeros
xp = zeros(pontos)
for i,t in enumerate(x):
    xp[i] = 0.5*(x[i]+x[-i])

plt.plot(vet,xp)
plt.show()







    