def function(x, f): return eval(f)


def Order1(func, x, h):
    x_retarded = (function(x, func) - function(x-h, func))/(h)
    x_centered = (function(x+h, func) - function(x-h, func))/(2*h)
    x_advanced = (function(x+h, func) - function(x, func))/(h)
    file_output.write("Retarded = {}\n" .format(x_retarded))
    file_output.write("Centered = {}\n" .format(x_centered))
    file_output.write("Advanced = {}\n\n" .format(x_advanced))


file_input = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/derivada-1ordem/input.txt', 'r')
file_output = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/derivada-1ordem/output.txt', 'w')

while(1):
    func = file_input.readline()
    x = int(file_input.readline())
    h = float(file_input.readline())
    Order1(func, x, h)
    if file_input.readline() == '':
        break

file_input.close()
file_output.close()
