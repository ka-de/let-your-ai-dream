import matplotlib.pyplot as plt
import numpy as np

# Define the higher-dimensional space
x = np.linspace(-20, 20, 2000)
y = np.linspace(-20, 20, 2000)
X, Y = np.meshgrid(x, y)

# Create a function representing a fractal-enriched mathematical enigma
fractal_enigma = (
    np.sin(np.sqrt(X**2 + Y**2)) * np.cos(0.6*X) * np.sin(0.8*Y) +
    0.5 * np.sin(0.3 * np.cos(0.7 * X) * np.sin(0.5 * np.cos(0.7 * Y)))
) * np.exp(-0.015 * (X**2 + Y**2))

# Plot the fractal-enriched mathematical enigma in a 3D space
fig = plt.figure(figsize=(18, 18))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, fractal_enigma, cmap='magma')

# Customize the plot for a creative journey
ax.set_title("Fractal-Enriched Mathematical Enigma")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.view_init(80, 20)  # Adjust the viewing angle for a creative perspective

# Show the plot
plt.show()