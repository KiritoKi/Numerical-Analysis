from math import *
# Return result using the value x in the function


def function(funcao, x):
    return eval(funcao)


def secant(a, b, f, epsilon, output_file):
    # if product of f(a) and f(b) yields a number less than 0
    # Means that there is a root in the interval [a, b],
    # So, we can calculate it
    if(function(f, a) * function(f, b) < 0):
        iteration = 1
        # Calculate root
        x = b - (function(f, b) * (b - a))/(function(f, b) - function(f, a))

    # stop-condition-loop
    # when the function result is less than the precision
        while(abs(function(f, x)) > epsilon):
            # exchanging values
            a = b
            b = x
            # Calculate root
            x = b - (function(f, b) * (b - a)) / \
                (function(f, b) - function(f, a))
    # Incrementing iterations
            iteration = iteration + 1
    # Print the results in the output.txt
        output_file.write("f(x) = {}" .format(str(f)))
        output_file.write("Iteration = {}\n" .format(str(iteration)))
        output_file.write("c = {} \n" .format(str(x)))
        output_file.write("f(c) = {}\n\n\n" .format(str(function(f, x))))

    else:
        output_file.write('Não existe raiz no intervalo inserido\n\n\n')


def main():

    # Opening Archs
    input_file = open(
        '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Secante/input.txt', 'r')
    output_file = open(
        '/home/kirito/Documentos/All-Scripts/Numerical Analysis/Secante/output.txt', 'w')
    while(1):
        # Read the function
        func = input_file.readline()
        # Read >a< Value
        a = float(input_file.readline())
        # Read >b< Value
        b = float(input_file.readline())
        # Read the accuracy
        epsilon = float(input_file.readline())
        # Applying Secant
        secant(a, b, func, epsilon, output_file)

        if(input_file.readline() == ""):
            break
    # Closing the archs
    input_file.close()
    output_file.close()


if __name__ == '__main__':
    main()
