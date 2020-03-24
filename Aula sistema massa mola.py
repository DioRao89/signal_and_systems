# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:48:43 2020

@author: Dionisio 

"""
# importar biblioteca matplot como plt
import matplotlib.pyplot as plt 
# da biblioteca numpy importa exp, seno e cosseno
from numpy import exp,sin,cos
#importar biblioteca numpy como np
import numpy as np
# criar objeto para o eixo horizontal
t = np.linspace(0,5,1000)
amplitude = 1
dieta= 1 #engorda ou emagrece a funcao
horizontal= 1 
vertical = 1
#questao piloto
x = amplitude*sin(dieta*t+horizontal)+vertical
plt.plot(t,x) #grava na memoria os vetores t e x
plt.show() # cria a imagem
#questao a
x = 15*exp(-2*t)-10*exp(-3*t)
plt.plot(t,x) #grava na memoria os vetores t e x
plt.show() # cria a imagem
#questao b
x = exp(-2*t)*(2-t)
plt.plot(t,x) #grava na memoria os vetores t e x
plt.show() # cria a imagem
