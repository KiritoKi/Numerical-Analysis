from math import e, pi, sqrt


def f(fun, x):
    return eval(fun)


def simpson(p, fun, n):
    h = (p[-1] - p[0])
    integration = 0
    p1 = [p[0]+(h/n)]

    for i in range(1, n-1):
        p1.append(p1[i-1]+(h/n))

    for i in p1:
        integration += 3 * f(fun, i)

    I = h*((f(fun, p[0]) + integration + f(fun, p[-1]))/8)
    file_output.write(f'I = {I}\n\n')


file_input = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/integral/Simpson de 3-8/input.txt', 'r')
file_output = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/integral/Simpson de 3-8/output.txt', 'w')

while(True):
    func = file_input.readline()
    p = [float(i)
         for i in file_input.readline().replace('\n', '').split(' ')]
    n = int(file_input.readline())

    simpson(p, func, n)

    if file_input.readline() == '':
        break
file_input.close()
file_output.close()
