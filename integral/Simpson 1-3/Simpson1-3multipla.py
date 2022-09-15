from math import e, pi, sqrt


def f(fun, x):
    return eval(fun)


def simpsonmult(pontos, func, n):
    h = (pontos[-1] - pontos[0])
    p = [pontos[0]]
    for i in range(1, n):
        p.append(p[i-1]+(h/n))
    p.append(pontos[-1])

    Sum = 0

    for i in range(1, n):
        if i % 2 == 0:  # if par
            Sum += 2 * f(func, p[i])
        else:  # if impar
            Sum += 4 * f(func, p[i])

    I = h*((f(func, pontos[0]) + Sum + f(func, pontos[-1]))/(3*n))

    file_output.write(f'I = {I}\n\n')


file_input = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/integral/Simpson de 1-3/input.txt', 'r')
file_output = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/integral/Simpson de 1-3/output.txt', 'w')

while(1):

    func = file_input.readline()
    pontos = [float(i)
              for i in file_input.readline().replace('\n', '').split(' ')]
    n = int(file_input.readline())

    simpsonmult(pontos, func, n)
    if file_input.readline() == '':
        break

file_input.close()
file_output.close()
