# calculates the norm between the vectors VX
def norm(V, X):
    # AUX
    previousNum, previousDen = 0, 0
    # search-loop to -->biggest denominator and numerator
    for i in range(len(V)):
        # Calculate atual numerator
        num = abs(V[i] - X[i])
        # Calculate denominator
        den = abs(V[i])
        # if num > previous numerator
        if num > previousNum:
            previousNum = num
        # if den > previous denominator
        if den > previousDen:
            previousDen = den
    # return division of the largest number by the largest denominator
    return previousNum/previousDen
# Soltion the system Ax=b


def seidel(n, A, B, epsilon, iter):
    # create vector x and v with A's size
    x = [0 for i in range(n)]
    v = [0 for i in range(n)]
    # Calculate value of each position matrix A and vector b ->>> i = row/column = j
    for i in range(n):
        for j in range(n):
            # If atual value does not in mainDiag
            # then the value of this position is changed to the value of division of your element
            # by the element of the main diagonal of your line
            if i != j:
                A[i][j] /= A[i][i]
        # b[i] will be assgned the division of your value
        # by the element of the main diagonal of your line
        B[i] /= A[i][i]
    # if k > iter
    for k in range(1, iter+1):
        # for row
        for i in range(n):
            # Sum
            sum = 0
            # for column
            for j in range(n):
                # if element != mainDiag
                # Sum += row * aprox
                if i != j:
                    sum += A[i][j] * x[j]
            # calculate the diference between b and sum
            x[i] = B[i] - sum
        # norm v and x
        result = norm(x, v)
        # if norm<= precision, end
        if result <= epsilon:
            return x
        # or v=x
        v = [i for i in x]


def main():

    # Opening archs
    input_file = open(
        '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Gauss-Seidel/input.txt', 'r')
    output_file = open(
        '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Gauss-Seidel/output.txt', 'w')
    # Creating empty vectors A and B
    A = []
    B = []
    # Reading the amount of rows
    size = int(input_file.readline())
    # Reading the epsilon
    epsilon = float(input_file.readline())
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
    # Applying the Gauss-Seidel and Print the results in the output.txt
    output_file.write(str(seidel(len(A), A, B, epsilon, 50)) + '\n')
    # Closing the archs
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
