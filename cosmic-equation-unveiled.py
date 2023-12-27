import matplotlib.pyplot as plt
import numpy as np

# Define the higher-dimensional space
x = np.linspace(-8, 8, 800)
y = np.linspace(-8, 8, 800)
X, Y = np.meshgrid(x, y)

# Create a function representing a cosmic equation
cosmic_equation = np.cos(np.sqrt(X**2 + Y**2)) * np.sin(X*Y) * np.exp(-0.1 * (X**2 + Y**2))

# Plot the cosmic equation in a 3D space
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, cosmic_equation, cmap='twilight')

# Customize the plot for an exploration of the unknown
ax.set_title("Cosmic Equation Unveiled")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.view_init(45, 60)  # Adjust the viewing angle for an exploration vibe

# Show the plot
plt.show()