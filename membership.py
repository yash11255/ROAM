pip install -U scikit-fuzzy
# Triangular function (without skfuzzy):#
import matplotlib.pyplot as plt
import numpy as np

# Triangular function
def triangular(x, a, b, c):
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

# Define parameters
a, b, c = 2, 4, 6

# Generate x values
x = np.linspace(0, 8, 100)

# Calculate membership function values
y_triangular = triangular(x, a, b, c)

# Plot the membership function curve
plt.plot(x, y_triangular, label='Triangular Function')
plt.title('Triangular Membership Function')
plt.xlabel('x')
plt.ylabel('Membership Value')
plt.legend()
plt.show()

#b) Gaussian function (without skfuzzy):#
# Gaussian function
def gaussian(x, mean, sigma):
    return np.exp(-0.5 * ((x - mean) / sigma) ** 2)

# Define parameters
mean, sigma = 4, 1.5

# Calculate membership function values
y_gaussian = gaussian(x, mean, sigma)

# Plot the membership function curve
plt.plot(x, y_gaussian, label='Gaussian Function')
plt.title('Gaussian Membership Function')
plt.xlabel('x')
plt.ylabel('Membership Value')
plt.legend()
plt.show()

#c) Trapezoid function (without skfuzzy):#
# Trapezoid function
def trapezoid(x, a, b, c, d):
    return np.maximum(0, np.minimum(np.minimum((x - a) / (b - a), 1, (d - x) / (d - c)), 1))

# Define parameters
a, b, c, d = 2, 3, 6, 7

# Calculate membership function values
y_trapezoid = trapezoid(x, a, b, c, d)

# Plot the membership function curve
plt.plot(x, y_trapezoid, label='Trapezoid Function')
plt.title('Trapezoid Membership Function')
plt.xlabel('x')
plt.ylabel('Membership Value')
plt.legend()
plt.show()






##Using skfuzzy:##
import skfuzzy as fuzz

# Define universe and fuzzy sets
x_universe = np.linspace(0, 8, 100)
triangular_membership = fuzz.trimf(x_universe, [2, 4, 6])
gaussian_membership = fuzz.gaussmf(x_universe, 4, 1.5)
trapezoid_membership = fuzz.trapmf(x_universe, [2, 3, 6, 7])

# Plot membership functions using skfuzzy
plt.plot(x_universe, triangular_membership, label='Triangular Function')
plt.plot(x_universe, gaussian_membership, label='Gaussian Function')
plt.plot(x_universe, trapezoid_membership, label='Trapezoid Function')

plt.title('Membership Functions using skfuzzy')
plt.xlabel('x')
plt.ylabel('Membership Value')
plt.legend()
plt.show()

