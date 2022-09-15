def function(x, f): return eval(f)


def Order2(func, x, h):
    x_retardada = (function(x, func) - 2*function(x-h, func) +
                   function(x-2*h, func))/(h**2)
    x_centrada = (function(x+h, func) - 2*function(x, func) +
                  function(x-h, func))/(h**2)
    x_avancada = (function(x+2*h, func) - 2 *
                  function(x+h, func) + function(x, func))/(h**2)
    file_output.write("Retardada = {}\n" .format(x_retardada))
    file_output.write("Centrada = {}\n" .format(x_centrada))
    file_output.write("Avancada = {}\n\n" .format(x_avancada))


file_input = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/derivada-2ordem/input.txt', 'r')
file_output = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/derivada-2ordem/output.txt', 'w')
while(1):
    func = file_input.readline()
    x = int(file_input.readline())
    h = float(file_input.readline())
    Order2(func, x, h)
    if file_input.readline() == '':
        break
file_input.close()
file_output.close()
