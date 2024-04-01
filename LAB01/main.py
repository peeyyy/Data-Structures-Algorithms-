import matplotlib.pyplot as plt
import ast
import math

valueX = [] # an empty list (valueX). Will be filled with values from a file yung 1-50 na x values

# choose_number variable dito mag choose muna kung anong function isolve from 1-10 and 11 para isolve lahat
choose_number = int(input("LIST OF FUNCTIONS:\n1.) f(x) = x^2 + 7x + 2\n2.) f(x) = 3x + 2\n3.) f(x) = x^2\n4.) f(x) = x^3\n5.) f(x) = x^5\n6.) f(x) = x^3 + 2x^2 + x + 10\n7.) f(x) = x^4 - 3x^3 + 2x^2 - x + 11\n8.) f(x) = sin(x)\n9.) f(x) = cos(x)\n10.) f(x) = x^5 + 4x^4 + x^3 - 2x^2 + 100\n11.) All Functions from 1-10\n\nEnter the number of the function you want to solve: "))

# list of string representations of the mathematical functions that the user can choose para sa graph
function_expressions = [
    "x^2 + 7x + 2",
    "3x + 2",
    "x^2",
    "x^3",
    "x^5",
    "x^3 + 2x^2 + x + 10",
    "x^4 - 3x^3 + 2x^2 - x + 11",
    "sin(x)",
    "cos(x)",
    "x^5 + 4x^4 + x^3 - 2x^2 + 100"]

with open('data_num.txt', 'r') as file: # iread niya yung 1-50 na x values 
    data = file.readlines() # basahin niya lahat ng lines galing sa file na 1-50 x values and stores them in the data variable
    for d in data:
        valueX.extend([int(value) for value in d.split(',')]) # splits each line at the commas, converts each resulting string to an integer, and adds these integers to the valueX list

# it calculates the 1st function [f(x) = x^2 + 7x + 2] for each value in valueX and returns a list of the results
def eq1():
    result = []
    for x in valueX:
        result.append((x**2) + (7 * x) + 2)
    return result

# 2nd function [f(x) = 3x + 2]
def eq2():
    result = []
    for x in valueX:
        result.append((3 * x) + 2)
    return result

# 3rd function [f(x) = x^2]
def eq3():
    result = []
    for x in valueX:
        result.append((x**2))
    return result

# 4th function [f(x) = x^3]
def eq4():
    result = []
    for x in valueX:
        result.append((x**3))
    return result

# 5th function [f(x) = x^5]
def eq5():
    result = []
    for x in valueX:
        result.append((x**5))
    return result

# 6th function [f(x) = x^3 + 2x^2 + x + 10]
def eq6():
    result = []
    for x in valueX:
        result.append((x**3) + (2 * x ** 2) + x + 10)
    return result

# 7th function [f(x) = x^4 - 3x^3 + 2x^2 - x + 11]
def eq7():
    result = []
    for x in valueX:
        result.append((x**4) - (3 * x ** 3) + (2 * x**2) - x + 11)
    return result

# 8th function [f(x) = sin(x)]
def eq8():
    result = []
    for x in valueX:
        result.append(math.sin(x))
    return result

# 9th function [f(x) = cos(x)]
def eq9():
    result = []
    for x in valueX:
        result.append(math.cos(x))
    return result

# 10th function [f(x) = x^5 + 4x^4 + x^3 - 2x^2 + 100]
def eq10():
    result = []
    for x in valueX:
        result.append((x**5) + (4 * x ** 4) + (x ** 3) - (2 * x ** 2) + 100)
    return result

def createFile(equation_number): 
    with open("function_result.txt", "w") as file: # opens the file function_result.txt in write mode
        if equation_number == 1: # uses if elif para malaman kung anong equation_number ang iapply ng user para ioverwrite sa function_result.txt
            file.write(str(eq1()))
        elif equation_number == 2:
            file.write(str(eq2()))
        elif equation_number == 3:
            file.write(str(eq3()))
        elif equation_number == 4:
            file.write(str(eq4()))
        elif equation_number == 5:
            file.write(str(eq5()))
        elif equation_number == 6:
            file.write(str(eq6()))
        elif equation_number == 7:
            file.write(str(eq7()))
        elif equation_number == 8:
            file.write(str(eq8()))
        elif equation_number == 9:
            file.write(str(eq9()))
        elif equation_number == 10:
            file.write(str(eq10()))
        elif equation_number == 11:
            file.write(str(eq1()))
            file.write("\n")
            file.write(str(eq2()))
            file.write("\n")
            file.write(str(eq3()))
            file.write("\n")
            file.write(str(eq4()))
            file.write("\n")
            file.write(str(eq5()))
            file.write("\n")
            file.write(str(eq6()))
            file.write("\n")
            file.write(str(eq7()))
            file.write("\n")
            file.write(str(eq8()))
            file.write("\n")
            file.write(str(eq9()))
            file.write("\n")
            file.write(str(eq10()))
# writes the result of the chosen function(s) to the file

def readfile():
    results = [] # empty list na lalagyan mga results read from the file
    with open("function_result.txt", "r") as file: # opens a file function_result.txt in read mode
        data = file.readlines()
        for line in data:
            results.append(ast.literal_eval(line.strip())) # removes leading and trailing whitespace from each line interprets the line as a Python literal and adds the resulting value to results.
    return results

def results_plot():
    if choose_number == 11:
        results = readfile() # calls the readfile function which reads the results of the mathematical functions from a file and returns them as a list
        for i, result in enumerate(results): # The enumerate function is used to get both the index (i) and the value (result) of each item
            # Use the function expressions in the labels
            plt.plot(valueX, result, label=f"Function {i+1}: {function_expressions[i]}")
            plt.title("Graph of All Functions")
    elif choose_number < 11:
        results = readfile()
        for i, result in enumerate(results): # The enumerate function is used to get both the index (i) and the value (result) of each item.
            # Use the function expressions in the labels
            plt.plot(valueX, result, label=f"Function {choose_number}: {function_expressions[choose_number - 1]}")
            plt.title(f"Graph of {function_expressions[choose_number - 1]}")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend(loc='best')
    plt.show()

createFile(choose_number) # writes the results of the chosen mathematical function(s) to a file
results_plot() # calls the function results_plot() to plot the graph