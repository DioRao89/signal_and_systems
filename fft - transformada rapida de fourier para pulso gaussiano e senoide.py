# -*- coding: utf-8 -*-
"""
Analise de modos de propagacao em uma dimensao. assim como a transformada de fourier. 
"""

import numpy as np #biblioteca de funcoes matematicas
from scipy.fftpack import fft,fftfreq # transformada rapida de fourier
import matplotlib.pyplot as plt # plotar grafico

# Number of sample points 
N = 6000 # QUANTIDADE DE PONTOS QUE SERAO CALCULADOS 
T = 1.0 / 1000.0 # # A DISTANCIA ENTRE CADA PONTO DE ANALISE (DISCRETIZACAO)
#linspace gera um vetor (lista) como se fosse um "for"
x = np.linspace(0.0, N*T, N) # GERA O EIXO HORIZONTAL (TEMPO)
#x = list(np.arange(0.0, N*T, N)) # nao permite o funcionamento do comando seguinte
sigma = 0.5 #largura do pulso gaussiano (inversamente proporcional a largura de banda)
centro = N*T/2
y = 2*np.exp(-((x-centro)**2)/sigma)
plt.plot(x,y)
plt.show()
f = 250
omega = 2.0*np.pi*f
fase = 0
amp = 2
# y -> sinal no tempo a ser alimentado na fibra
z = amp*np.sin(fase+omega*x)
#4*np.sin(np.pi/2+10*2.0*np.pi*x)
# amplitude(deslocamento vertical)*np.sin(frequencia(deslocamento horizontal na transformada) * 2.0*np.pi*x) 
plt.plot(x,z)
plt.show()

w = y*z

plt.plot(x,w,x,y)
plt.show()


yf = fft(z) # transformada de fourier
xf = np.linspace(0.0, 1.0/(2.0*T), N//2) #eixo horizontal no dominio da freq
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2])) #sinal no dominio da frequencia
plt.show()



"""
#dever de casa: gere prints e escreva
seus pensamentos coloque tudo num pdf. 

1) analise o Pulso Gaussiano do dominio 
da frequencia e explique
a) qual o comportamento grafico
b) qual o efeito da variavel 'centro'
c) qual o efeito da amplitude 
d) qual o efeito da variavel 'sigma'

2) analise sinal senoidal no dominio
da frequencia e explique
a) qual o comportamento grafico
b) qual o efeito da variavel 'frequencia'.
c) qual o efeito da amplitude 
d) qual o efeito da variavel 'fase'
















