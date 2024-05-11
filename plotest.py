import numpy as np

import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
data = np.random.randint(5, 20, size=10)

# Create x-axis values
x = np.arange(len(data))

# Plot the bar chart
plt.bar(x, data)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Random Bar Plot')

# Show the plot
plt.show()