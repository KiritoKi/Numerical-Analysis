# Metodo de Fatoração LU explicada no Relatório 1
I = []


def matriz_LU(size, A):
    for k in range(size):
        for i in range(k+1, size):
            # Calculate multiplicator of row
            m = A[i][k] / A[k][k]
            # Zeroing values below mainDiag
            A[i][k] = 0.0
            # filling matrix L (identity) below mainDiag with values m(multiplicator row)
            I[i][k] = m
            # filling matrix U into mainDiag and above
            for j in range(k+1, size):
                # the value of position j of each line.
                A[i][j] = A[i][j] - (m * A[k][j])

    return A

# pivoting and changing lines


def pivo(size, A, B):
    for i in range(size):
        for j in range(i+1, size):
            if(abs(A[i][i]) < abs(A[j][i])):
                aux = A[i]
                A[i] = A[j]
                A[j] = aux
                aux1 = B[i]
                B[i] = B[j]
                B[j] = aux1


def lu(size, A, B):
    global I
    # filling matrix I of the main diagonal with 1(Identity)
    for i in range(size):
        linha_I = [0.0]*size
        for j in range(size):
            if(i == j):
                linha_I[j] = 1.0
        I.append(linha_I)

    pivo(size, A, B)
    # Zeroing values below mainDiag = matrix U = matrix A
    # values of mainDiag and above = matrix L = matrix I
    aU = matriz_LU(size, A)
    aL = I

    y = [0.0]*size
    x = [0.0]*size
    y[0] = B[0] / aL[0][0]

    for i in range(1, size):
        s = 0.0
        for j in range(size):
            s = s + (aL[i][j] * y[j])
        y[i] = (B[i] - s) / aL[i][i]

    x[size-1] = y[size-1] / aU[size-1][size-1]
    for i in range(size-1, -1, -1):
        s = 0.0
        for j in range(i+1, size):
            s = s + (aU[i][j] * x[j])
        x[i] = (y[i] - s) / aU[i][i]

    return x
