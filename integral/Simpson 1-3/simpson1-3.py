from math import e, pi, sqrt


def funcction(func, x):
    return eval(func)


def simpson(p, func):
    h = (p[-1] - p[0])
    I = h*((funcction(func, p[0]) + 4 *
           funcction(func, h/2) + funcction(func, p[-1]))/6)
    file_output.write(f'I = {I}\n\n')


file_input = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/integral/Simpson de 1-3/input.txt', 'r')
file_output = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/integral/Simpson de 1-3/output.txt', 'w')

while(True):

    funcc = file_input.readline()
    p = [float(i) for i in file_input.readline().replace('\n', '').split(' ')]
    n = int(file_input.readline())

    simpson(p, funcc)
    if file_input.readline() == '':
        break
file_input.close()
file_output.close()
