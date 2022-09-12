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

# Transforming into a triangular matrix, zeroing the numbers below mainDiagonal


def mainDiagonal(size, A, B):
    # Calling pivot
    pivot(size, A, B)
    # Triangulation
    for k in range(size):
        if k == size-1:
            k = k - 1
        for i in range(k+1, size):
            # Define the multiplicator of row
            m = A[i][k] / A[k][k]
            A[i][k] = 0
            for j in range(k+1, size):
                # a row minus multiplicator by line pivot
                # do multiplicador da line pela line do pivô.
                A[i][j] = A[i][j] - (m * A[k][j])
            # the same process with B
            B[i] = B[i] - (m * B[k])


def gauss(size, A, B, X):
    # Elimination by calling mainDiagonal
    mainDiagonal(size, A, B)

    X[size-1] = B[size-1] / A[size-1][size-1]

    for i in range(size-1, -1, -1):
        s = 0.0
        for j in range(i+1, size):
            s = s + (A[i][j] * X[j])
            # Extract the result values in matrix
            X[i] = (B[i] - s) / A[i][i]
    # Vector X
    return X


def main():
    # Opening archs
    input_file = open(
        '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Eliminação de Gauss/input.txt', 'r')
    output_file = open(
        '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Eliminação de Gauss/output.txt', 'w')
    # Creating empty vectors A and B
    A = []
    B = []
    # Reading the amount of rows
    size = int(input_file.readline())
    # Creating a list of size
    X = [0.0]*size
    # Line by line loop
    for i in range(size):
        # List to store the float values ​​of a row
        line = []
        # Read the row numbers like a string value
        line_values = input_file.readline()
        # Remove the '\n'
        line_values = (line_values.replace('\n', ''))
        # Split the string into values
        line_values = line_values.split(' ')
        # store the values ​​of line_values in the line like a float values
        for j in range(len(line_values)-1):
            line.append(float(line_values[j]))
        # Store the last column B in B
        B.append(float(line_values[j+1]))
        # Stores the values of line in A column by column except the last column
        A.append(line)
    # Applying the Gauss and Print the results in the output.txt
    output_file.write(str(gauss(size, A, B, X)) + '\n')
    # Closing the archs
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
