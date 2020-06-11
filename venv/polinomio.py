import numpy as np
from scipy import linalg
from scipy import interpolate

print("Para usar métodos matemáticos use np. antes do que pretende\n Por exemplo np.exp() para calcular e^")
tamanho = int(input("Quantos pontos vai indicar: "))
Matriz = np.empty((tamanho, tamanho))
xi = np.empty((tamanho))
yi = np.empty((tamanho))
for x in range(tamanho):
    xi[x] = float(input("Indique o xi: "))
    yi[x] = float(eval(input("Indique o yi: ")))
for i in range(tamanho):
    for j in range(tamanho):
        Matriz[i][j] = xi[i] ** j
print(Matriz)
b=yi
Polinomio = linalg.solve(Matriz,b)
Resultado = "Polinomio = "
for i in range(tamanho-1,-1,-1):
    if(i==0):
        Resultado = Resultado + "{0}".format(Polinomio[i])
    else:
        Resultado = Resultado + "{0} x^ {1} + ".format(Polinomio[i],i)
print(Resultado)