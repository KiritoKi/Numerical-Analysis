from math import e, pi, sqrt


def function(f, x): return eval(f)


def trapezio(x0, func):
    h = x0[-1] - x0[0]
    I = h*((function(func, x0[0]) + function(func, x0[-1]))/2)
    return I


file_input = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/integral/Metodo do trapezio multiplo/input.txt', 'r')
file_output = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/integral/Metodo do trapezio multiplo/output.txt', 'w')

while(1):

    func = file_input.readline().replace('\n', '')
    x = [float(i) for i in file_input.readline().replace('\n', '').split(' ')]

    file_output.write("I = {}\n".format(str(trapezio(x, func))))
    file_output.write("{} Trapézios\n\n".format(str(len(x)-1)))

    if file_input.readline() == '':
        break

file_input.close()
file_output.close()
