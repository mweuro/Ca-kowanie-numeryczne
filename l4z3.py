import numpy as np
import math
import matplotlib.pyplot as plt

f = lambda x : x**3*math.exp(x)
a = -2
b = 2
teor = 2*(19 + math.exp(4))/math.exp(2)

def metoda1(a, b, n, f):
    c = np.linspace(a, b, n)
    h = (b - a)/(n - 1)
    d = [f((c[i] + c[i + 1])/2) for i in range(n - 1)]
    S = h*sum(d)
    return S

def metoda2(a, b, n, f):
    c = np.linspace(a, b, n)
    h = (b - a)/(n - 1)
    d = [f(c[i]) + f(c[i + 1]) for i in range(n - 1)]
    S = h/2*sum(d)
    return S

def metoda3(a, b, n, f):
    c = np.linspace(a, b, n)
    h = (b - a)/(n - 1)
    d = [f(c[i]) + 4*f((c[i] + c[i + 1])/2) + f(c[i + 1]) for i in range(n - 1)]
    S = h/6*sum(d)
    return S

n = np.array([10, 20, 50, 100, 200])
h = (b - a)/(n - 1)
X = np.log(h)

Y1 = np.log(np.array([abs(teor - metoda1(a, b, i, f)) for i in n]))
Y2 = np.log(np.array([abs(teor - metoda2(a, b, i, f)) for i in n]))
Y3 = np.log(np.array([abs(teor - metoda3(a, b, i, f)) for i in n]))

x1, y1 = np.polyfit(X, Y1, 1)
x2, y2 = np.polyfit(X, Y2, 1)
x3, y3 = np.polyfit(X, Y3, 1)

print('Metoda punktu środkowego: ' + str(metoda1(a, b, 200, f)))
print('Rząd zbieżności: ' + str(x1))
print('Metoda trapezów: ' + str(metoda2(a, b, 200, f)))
print('Rząd zbieżności: ' + str(x2))
print('Metoda Simpsona: ' + str(metoda3(a, b, 200, f)))
print('Rząd zbieżności: ' + str(x3))

v1 = [metoda1(a, b, n, f) for n in n]
v2 = [metoda2(a, b, n, f) for n in n]
v3 = [metoda3(a, b, n, f) for n in n]

plt.plot(n, v1, color = 'red', label = 'Metoda prostokąta')
plt.plot(n, v2, color = 'blue', label = 'Metoda trapezu', linestyle = '-.')
plt.plot(n, v3, color = 'green', label = 'Metoda Simpsona', alpha = 0.5)
plt.legend()
# plt.show()