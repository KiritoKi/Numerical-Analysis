from sympy import Symbol, sympify, integrate

# Matriz K and Matriz F Resolutions


def matrizes(grau, inter_a, inter_b, func):
    x = Symbol('x')
    for col in range(grau+1):
        line = [0.0] * (grau+1)
        for lin in range(grau+1):
            line[lin] = integrate(((x**lin) * (x**col)),
                                  (x, inter_a, inter_b))
        Matriz_f[col] = integrate(
            (sympify(func) * (x**col)), (x, inter_a, inter_b))
        Matriz_k.append(line)


def triangulation(grau, Matriz_k, Matriz_f):
    for k in range(grau+1):
        if k == grau-1:
            k = k - 1
        for i in range(k+1, grau+1):
            m = Matriz_k[i][k] / Matriz_k[k][k]
            Matriz_k[i][k] = 0
            for j in range(k+1, grau+1):
                Matriz_k[i][j] = Matriz_k[i][j] - (m * Matriz_k[k][j])

            Matriz_f[i] = Matriz_f[i] - (m * Matriz_f[k])


def mmq(grau, Matriz_k, Matriz_f, func):
    matrizes(grau, inter_a, inter_b, func)
    triangulation(grau, Matriz_k, Matriz_f)

    X = [0.0] * (grau+1)
    X[grau] = Matriz_f[grau] / Matriz_k[grau][grau]
    for i in range(grau, -1, -1):
        s = 0.0
        for j in range(i+1, grau+1):
            s = s + (Matriz_k[i][j] * X[j])
            X[i] = (Matriz_f[i] - s) / Matriz_k[i][i]

    return X


file_in = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/MMQ-continuo/input.txt', 'r')
file_out = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/MMQ-continuo/output.txt', 'w')

while(True):
    # Reads the function
    func = file_in.readline()
    # Read interval a
    inter_a = int(file_in.readline())
    # read interval b
    inter_b = int(file_in.readline())
    # Read
    grau = int(file_in.readline())
    # Matriz K
    Matriz_k = []
    # Matriz F
    Matriz_f = [0.0] * (grau+1)
    # Applying MMQ Continuous
    a = mmq(grau, Matriz_k, Matriz_f, func)
    x = Symbol('x')
    # Stores into Result the polynomial and write output file
    result = 0
    for i in range(grau+1):
        result = result + a[i]*x**i
    file_out.write("P(x) = {}\n\n" .format(result))
    # When reach the end o'arch
    if file_in.readline() == '':
        break

file_in.close()
file_in.close()
