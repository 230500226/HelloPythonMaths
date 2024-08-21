import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Create a figure and axis
fig, ax = plt.subplots()

# Plot a simple line
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
ax.plot(x, y)

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Hello Matplotlib!')

# Show the plot
plt.show()