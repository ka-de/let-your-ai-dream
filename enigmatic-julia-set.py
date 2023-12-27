import matplotlib.pyplot as plt
import numpy as np

def complex_function(z, c):
    return z**2 + c

def iterate_julia_set(width, height, xmin, xmax, ymin, ymax, c, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    img = np.zeros(Z.shape, dtype=float)

    for i in range(max_iter):
        mask = np.abs(Z) < 1000
        Z[mask] = complex_function(Z[mask], c)
        img += mask

    return img

# Set parameters for the Julia set on a larger canvas
width, height = 1200, 1200
xmin, xmax = -2.5, 2.5
ymin, ymax = -2.5, 2.5
c = complex(-0.7269, 0.1889)
max_iter = 100

# Generate an even more enigmatic Julia set
julia_img = iterate_julia_set(width, height, xmin, xmax, ymin, ymax, c, max_iter)

# Save the plot as a high-resolution image
plt.figure(figsize=(12, 12))
plt.imshow(julia_img, extent=(xmin, xmax, ymin, ymax), cmap='magma', origin='lower')
plt.title(f'Mathematical Expression: $z \\mapsto z^2 + {c}$')
plt.xlabel('Re')
plt.ylabel('Im')
plt.colorbar()

# Save the plot as a PNG file with higher DPI
plt.savefig('enigmatic_julia_set.png', dpi=300)

# Show the plot
plt.show()