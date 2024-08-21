import numpy as np
from scipy.fft import fft

# Function to evaluate the user-defined function
def evaluate_function(func_str, x_values):
	func = eval(f"lambda x: {func_str}")
	return np.array([func(x) for x in x_values])

# Get user input for the function
user_function = input("Enter a mathematical function of x (e.g., 'np.sin(x)'): ")

# Define the range and number of points
start = float(input("Enter the start of the range: "))
end = float(input("Enter the end of the range: "))
num_points = int(input("Enter the number of points: "))

# Generate x values
x_values = np.linspace(start, end, num_points)

# Evaluate the function over the range
input_array = evaluate_function(user_function, x_values)

# Calculate Fourier series using scipy's fft function
fourier_series = fft(input_array)

# Print the Fourier series
print("Fourier series:", fourier_series)