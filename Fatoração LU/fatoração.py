def pivot(size, A, B):
    # pivoting and changing lines
    for i in range(size):
        for j in range(i+1, size):
            if(abs(A[i][i]) < abs(A[j][i])):
                aux = A[i]
                A[i] = A[j]
                A[j] = aux
                aux1 = B[i]
                B[i] = B[j]
                B[j] = aux1


def matriz_LU(size, A, I):
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
    matrizes = [A, I]
    return matrizes


def lu(size, A, I, B):
    pivot(size, A, B)
    # Zeroing values below mainDiag = matrix U = matrix A
    # values of mainDiag and above = matrix L = matrix I
    aU, aL = matriz_LU(size, A, I)

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
    # Return X
    return x


def main():

    # Opening Archs
    input_file = open(
        '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Fatoração LU/input.txt', 'r')
    output_file = open(
        '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Fatoração LU/output.txt', 'w')
    # Creating empty vectors A and B
    A = []
    B = []
    # Reading the amount of rows
    size = int(input_file.readline())
    # Line by line loop
    for i in range(size):
        # List to store the float values ​​of a row
        linha = []
        # Read the row numbers like a string value
        line_values = input_file.readline()
        # Remove the '\n'
        line_values = (line_values.replace('\n', ''))
        # Split the string into values
        line_values = line_values.split(' ')
        # store the values ​​of line_values in the line like a float values
        for j in range(len(line_values)-1):
            linha.append(float(line_values[j]))
        # Store the last column B in B
        B.append(float(line_values[j+1]))
        # Stores the values of line in A column by column except the last column
        A.append(linha)
    # Creating a list I
    I = []
    # filling matrix I of the main diagonal with 1(Identity)
    for i in range(size):
        linha_I = [0.0]*size
        for j in range(size):
            if(i == j):
                linha_I[j] = 1.0
        I.append(linha_I)
    # Applying the LU and Print the results in the output.txt
    output_file.write(str(lu(size, A, I, B)) + '\n')
    # Closing the archs
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
