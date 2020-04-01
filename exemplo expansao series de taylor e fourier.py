from numpy import linspace, zeros, sin
import matplotlib.pyplot as plt 
pontos = 1000
inf = 0 
sup = 20
x = linspace(inf,sup,pontos)
f0 = zeros(pontos)
f1 = zeros(pontos)
f2 = zeros(pontos)
for i,_ in enumerate(x):
    f0[i] = -16

f1 = -26*x+36
f2 = x**2-30*x+40

plt.plot(x,f0,x,f1,x,f2)
plt.show()
#f(x) = 2sen(x) + 7sen(2x) + 5sen(3x) + 4sen(4x)
ft = zeros(pontos)
#editar essa parte para construir onda quadrada
ft = 2*sin(x) + 7*sin(2*x) + 5*sin(3*x) + 4*sin(4*x)
plt.plot(x,ft)
plt.show()


"""
Ex.
F(x)  -16
F’(x) = -26x+36
F’’(x) = x^2-30x+40

"""