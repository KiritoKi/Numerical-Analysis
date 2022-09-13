from math import e, pi, tan, sin, cos
from sympy import diff
# Return result using the value x in the function


def function(funcao, x):
    return eval(funcao)


def newton(a, b, f, diff_f, epsilon, output_file):
    # if product of f(a) and f(b) yields a number less than 0
    # Means that there is a root in the interval [a, b],
    # So, we can calculate it
    if(function(f, a) * function(f, b) < 0):
        iteration = 1
        # MidPoint
        x1 = (a+b)/2
        # stop-condition-loop
        # when the function result is less than the precision
        while(abs(function(f, x1)) > epsilon):
            # Calculate root
            x1 = x1 - (function(f, x1)/function(diff_f, x1))
            # Incrementing iterations
            iteration = iteration + 1
        # Print the results in the output.txt
        output_file.write("f(x) = {}" .format(str(f)))
        output_file.write("Iteration = {}\n" .format(str(iteration)))
        output_file.write("c = {} \n" .format(str(x1)))
        output_file.write("f(c) = {}\n\n\n" .format(str(function(f, x1))))

    else:
        output_file.write('Não existe raiz no intervalo inserido\n\n\n')


def main():
    # Opening Archs
    input_file = open(
        '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Newton Raphson/input.txt', 'r')
    output_file = open(
        '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Newton Raphson/output.txt', 'w')
    while(True):
        # Read the Function
        func = input_file.readline()
        # Read >a< value
        a = float(input_file.readline())
        # Read >a< value
        b = float(input_file.readline())
        # Read the accuracy
        epsilon = float(input_file.readline())
        # Applying Newton

        newton(a, b, func, str(diff(func)), epsilon, output_file)

        if(input_file.readline() == ""):
            break
    # Closing the Archs
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
