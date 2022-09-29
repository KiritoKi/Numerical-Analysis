from sympy import Symbol, simplify, expand


def Newton(x, y, n):
    X = Symbol('x')
    Next = 1
    table = [y]
    result = 0
    grau = 0
    # each execution, insert a new order in table to the last resulted order
    for i in range(n-1):
        ordem = []
        for j in range(len(table[i]) - 1):
            dif_divided = (table[i][j+1] - table[i][j])/(x[j+Next] - x[j])
            ordem.append(dif_divided)
        table.append(ordem)
        Next += 1

    for i in range(len(table)):
        fator = table[i][0]
        for j in range(grau):
            fator *= (X - x[j])
        grau += 1
        result += fator

    P = simplify(result)
    P = expand(P)
    file_output.write(f'Px = {P}\n\n')


file_input = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/Interpolação/Método de newton/input.txt', 'r')
file_output = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/Interpolação/Método de newton/output.txt', 'w')

while(True):
    x = [float(i) for i in file_input.readline().replace('\n', '').split(' ')]
    y = [float(i) for i in file_input.readline().replace('\n', '').split(' ')]

    Newton(x, y, len(x))

    if file_input.readline() == '':
        break

file_input.close()
file_output.close()
