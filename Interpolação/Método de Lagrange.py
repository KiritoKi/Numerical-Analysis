from sympy import Symbol, simplify, expand
import matplotlib.pyplot as mp


def lagrange(x, y, n):
    X = Symbol('x')
    l = []
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (X - x[j])/(x[i] - x[j])
        l.append(L)
    s = 0
    # Somatório de f(x)k*lk
    for i in range(len(l)):
        s += y[i]*l[i]
    # To resolve it = simplify
    P = simplify(s)
    P = expand(s)

    def funcao(x): return eval(str(P))
    res = [funcao(ponto) for ponto in x]
    mp.plot(x, y, 'bo')
    mp.plot(x, res)

    mp.show()

    file_output.write("Px = {}\n\n" .format(P))


file_input = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/Interpolação/Método de Lagrange/input.txt', 'r')
file_output = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/Interpolação/Método de Lagrange/output.txt', 'w')

while(True):
    x = [float(i) for i in file_input.readline().replace('\n', '').split(' ')]
    y = [float(i) for i in file_input.readline().replace('\n', '').split(' ')]

    lagrange(x, y, len(x))
    # When reach the end o'arch
    if file_input.readline() == '':
        break


file_input.close()
file_output.close()
