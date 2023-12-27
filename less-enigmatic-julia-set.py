import matplotlib.pyplot as plt
import numpy as np

def julia_set(width, height, xmin, xmax, ymin, ymax, c, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    img = np.zeros(Z.shape, dtype=float)

    for i in range(max_iter):
        mask = np.abs(Z) < 1000
        Z[mask] = Z[mask]**2 + c
        img += mask

    return img

# Set parameters for the Julia set
width, height = 800, 800
xmin, xmax = -2, 2
ymin, ymax = -2, 2
c = complex(-0.8, 0.156)
max_iter = 100

# Generate the more enigmatic Julia set
julia_img = julia_set(width, height, xmin, xmax, ymin, ymax, c, max_iter)

# Plot the Julia set
plt.figure(figsize=(8, 8))
plt.imshow(julia_img, extent=(xmin, xmax, ymin, ymax), cmap='plasma', origin='lower')
plt.title(f'Enigmatic Julia Set for c = {c}')
plt.xlabel('Re')
plt.ylabel('Im')
plt.colorbar()

# Show the plot
plt.show()