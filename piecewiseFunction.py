import numpy as np
import matplotlib.pyplot as plt

def piecewise_function(x, conditions, functions):
    for condition, function in zip(conditions, functions):
        if eval(condition):
            return eval(function)
    return None  # Return None if no condition is met

# Get user input for the piecewise function
function_input = input("Enter the piecewise function in the format 'x^2, 0<x<2, x, 2<x<3': ")

# Replace '^' with '**' for exponentiation
function_input = function_input.replace('^', '**')

# Parse the input
functions_conditions = function_input.split(', ')
functions = functions_conditions[::2]
conditions = functions_conditions[1::2]

# Print confirmation of the piecewise function
print("Piecewise function:")
for function, condition in zip(functions, conditions):
    print(f"f(x) = {function} for {condition}")

# Create a numpy array of x values
x = np.linspace(-10, 10, 1000)

# Evaluate the piecewise function for each x value
y = np.array([piecewise_function(val, conditions, functions) for val in x])

# Filter out None values
x_filtered = x[y != None]
y_filtered = y[y != None]

# Plot the piecewise function
plt.plot(x_filtered, y_filtered)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Piecewise Function')
plt.grid(True)
plt.show()