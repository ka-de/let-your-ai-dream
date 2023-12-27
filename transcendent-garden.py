import matplotlib.pyplot as plt
import numpy as np

# Define the higher-dimensional space
x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)

# Create a function representing the mathematical equations
equation = np.sin(np.sqrt(X**2 + Y**2)) * np.exp(-0.1 * (X**2 + Y**2))

# Plot the mathematical blooms in a 3D space
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, equation, cmap='viridis')

# Customize the plot for a surreal atmosphere
ax.set_title("Transcendent Garden of Equations and Waves")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.view_init(30, 45)  # Adjust the viewing angle for a captivating perspective

# Show the plot
plt.show()