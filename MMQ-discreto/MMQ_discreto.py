from sympy import Symbol
from lu import lu


def mmq(x, y, grau):
    matriz = []
    # grau+1 cause for example grau=2 -> 1 +a1*x +a2*x²
    # then there are three elements into µatriz line
    # Create sets matriz:
    # [ 1, 1, 1,       ..., 1 ]
    # [ x0¹, x1¹, x2¹, ..., xn¹ ] n = last X
    # [ x0², x1², x2², ..., xn²]           .
    #              .
    #              .
    # [ x0^m, x1^m, x2^m, ..., xn^m ] m = grau
    matriz = [[j**i for j in x] for i in range(grau+1)]
    v = ScalarProductPartY(matriz, y)
    c = ScalarProductPartMatriz(matriz)
    # Applying LU
    a = lu(len(matriz), c, v)
    # Creates Symbol X
    x = Symbol('x')
    result = 0
    # Stores into Result the polynomial and write output file
    for i in range(grau+1):
        result += a[i]*x**i
    output_file.write("P(x) = {}\n\n" .format(result))

# Sum of all y * each line of column
# temp = [Scalar Product y -> u0; y -> u1; ...] (uj = set of xj)


def ScalarProductPartY(Matriz, y):
    temp = []
    for i in range(len(Matriz)):
        temp.append(sum([y[j]*Matriz[i][j] for j in range(len(y))]))

    return temp

# ScalarProduct of Matriz
# Return Lists (Matriz)


def ScalarProductPartMatriz(Matriz):
    temp = []
    for i in range(len(Matriz)):
        temp.append([prod(Matriz, j, i) for j in range(len(Matriz))])
    return temp

# Product


def prod(matriz, x, y):
    aux = []
    for i in range(len(matriz[0])):
        aux.append(matriz[x][i] * matriz[y][i])
    return sum(aux)


input_file = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/MMQ-discreto/input.txt', 'r')
output_file = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/MMQ-discreto/output.txt', 'w')

while(True):
    # Reads line of X and Convert to float<
    x = [float(i) for i in input_file.readline().replace('\n', '').split(' ')]
    # Reads line of Y and Convert to float<
    y = [float(i) for i in input_file.readline().replace('\n', '').split(' ')]
    # Reads grau and Convert to int
    grau = int(input_file.readline())

    # Apply mmq
    mmq(x, y, grau)
    # When reach the end o'arch
    if input_file.readline() == '':
        break

input_file.close()
output_file.close()
