def linearRegression(n, x, y):
    # initialize with 0 values
    sumXY = 0.0
    sumXquadrado = 0.0

    for i in range(n):
        sumXY = sumXY + (x[i]*y[i])
        sumXquadrado = sumXquadrado + (x[i]**2)
    # Calculate a1
    a1 = ((n * sumXY) - (sum(x) * sum(y))) / \
        ((n * sumXquadrado) - (sum(x) ** 2))
    # Calculate a0
    a0 = ((sum(y) * sumXquadrado) - (sum(x) * sumXY)) / \
        ((n * sumXquadrado) - (sum(x) ** 2))
    #ymedio = sum(y)/n
    #xmedio = sum(x)/n
    #a0 = ymedio - (a1*xmedio)
    # y = a0 + a1x
    output_file.write("y = {} + {}x\n".format(a0, a1))
    output_file.write("Pontos X = {}\n" .format(x))
    output_file.write("Pontos Y = {}\n\n" .format(y))


input_file = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/regressão linear/input.txt', 'r')
output_file = open(
    '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Relatorio-2/regressão linear/output.txt', 'w')

while(True):
    # Reads line of X
    x = input_file.readline().replace('\n', '').split(' ')
    # Reads line of Y
    y = input_file.readline().replace('\n', '').split(' ')
    # Convert to float<
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    # Apply Linear Regression
    linearRegression(len(x), x, y)
    # When reach the end o'arch
    if input_file.readline() == '':
        break

input_file.close()
output_file.close()
