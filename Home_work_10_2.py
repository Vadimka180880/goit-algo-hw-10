import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return np.sin(x)

a = 0  # Нижня межа
b = np.pi  # Верхня межа

# Крок 1: Побудова графіка
x = np.linspace(-0.5, 3.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)

ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

ax.set_xlim([x[0], x[-1]])
ax.set_ylim([min(y) - 0.1, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = sin(x) від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

# Крок 2: Метод Монте-Карло
N = 100000
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, 1, N)  # f(b) = sin(pi) = 0, максимальне значення sin(x) на інтервалі [0, pi] = 1

under_curve = y_random < f(x_random)
integral_mc = (b - a) * 1 * np.sum(under_curve) / N

print("Інтеграл методом Монте-Карло: ", integral_mc)

# Крок 3: SciPy
result, error = spi.quad(f, a, b)
print("Інтеграл за допомогою SciPy: ", result)
print("Оцінка абсолютної помилки: ", error)

# Аналітичний результат
analytical_result = -np.cos(b) + np.cos(a)
print("Аналітичний результат: ", analytical_result)
