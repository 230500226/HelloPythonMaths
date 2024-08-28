import sympy as sp

def generate_values():
    # Define the variable 't'
    t = sp.symbols('t')
    values = []
    # Loop from 0 to 6
    for i in range(0, 7):
        # Define x(t) = t + 6
        x_t = t + 6
        # Integrate x(t) from -6 to i
        value = sp.integrate(x_t, (t, -6, i))
        values.append(value)
    return values

# Define the variable 't'
t = sp.symbols('t')
# Generate the list of integrated values
result = generate_values()
# Print the list of integrated values
print(result)
# Define x(t) = t + 6
x_t = t + 6
# Multiply x(t) by DiracDelta(t + 4)
multiplied_value = x_t * sp.DiracDelta(t + 4)
# Integrate the multiplied value from -6 to 6
integral = sp.integrate(multiplied_value, (t, -6, 6))
# Print the result of the integration
print(integral)