import matplotlib.pyplot as plt
import numpy as np

# Define the higher-dimensional space
x = np.linspace(-12, 12, 1200)
y = np.linspace(-12, 12, 1200)
X, Y = np.meshgrid(x, y)

# Create a function representing an enigmatic fractal composition
fractal_composition = np.sin(np.sqrt(X**2 + Y**2)) * np.cos(0.7*X) * np.sin(0.5*Y) * np.exp(-0.03 * (X**2 + Y**2))

# Plot the enigmatic fractal composition in a 3D space
fig = plt.figure(figsize=(14, 14))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, fractal_composition, cmap='plasma')

# Customize the plot for an exploration into the enigma
ax.set_title("Enigmatic Fractal Composition")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.view_init(60, 45)  # Adjust the viewing angle for an enigmatic perspective

# Show the plot
plt.show()