import numpy as np

def main():
    print("Hello, World!")
    
    # Prompt the user to input numbers
    user_input = input("Enter numbers separated by spaces: ")
    
    # Convert the input string to a list of floats
    numbers = list(map(float, user_input.split()))
    
    # Convert the list to a NumPy array
    np_array = np.array(numbers)
    
    # Perform calculations
    total_sum = np.sum(np_array)
    mean_value = np.mean(np_array)
    
    # Print the results
    print(f"Sum of the numbers: {total_sum}")
    print(f"Mean of the numbers: {mean_value}")

if __name__ == "__main__":
    main()