import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Definir la función que queremos integrar
def f(x):
    return np.exp(-x**2)

# Integrar la función
result, error = quad(f, -np.inf, np.inf)

# Mostrar el resultado
print("Resultado de la integral: ", result)
print("Error: ", error)

# Graficar la función y la integral aproximada
x = np.linspace(-10, 10, 400)
y = f(x)

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='f(x) = e^(-x^2)')
plt.plot(x, result*np.exp(-x**2), label='Integral aproximada')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Integral de f(x) = e^(-x^2)')
plt.legend()
plt.show()