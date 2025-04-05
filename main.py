import numpy as np
import matplotlib.pyplot as plt

# Вихідні дані
m = 1
A = -m  # Амплітуда
omega = 5.65  # Кутова частота
phi = np.pi / m  # Фаза
Td = 0.1  # Період дискретизації
N = 10  # Кількість відліків

# Часові моменти для аналогового сигналу
t_analog = np.linspace(0, N * Td, 1000)
x_analog = A * np.cos(omega * t_analog + phi)

# Дискретизація сигналу
n = np.arange(N)
t_discrete = n * Td
x_discrete = A * np.cos(omega * t_discrete + phi)

# Відновлення сигналу
K = 10
t_reconstructed = np.linspace(0, N * Td, 1000)
x_reconstructed = np.zeros_like(t_reconstructed)

for k in range(K):
    x_reconstructed += x_discrete[k] * np.sinc(np.pi * (t_reconstructed / Td - k))

# ---------------------------------------------------------------------------
# Синя лінія: аналоговий сигнал x(t).
# Червоні точки: дискретні відліки x(nTd).
# Зелена пунктирна лінія: відновлений сигнал за допомогою інтерполяції sinc.
# ---------------------------------------------------------------------------

plt.figure(figsize=(10, 6))
plt.plot(t_analog, x_analog, 'b-', label='Аналоговий сигнал')
plt.stem(t_discrete, x_discrete, linefmt='r-', markerfmt='ro', basefmt=' ', label='Дискретні відліки')
plt.plot(t_reconstructed, x_reconstructed, 'g--', label='Відновлений сигнал')


plt.title('Дискретизація та відновлення сигналу')
plt.xlabel('Час (с)')
plt.ylabel('Амплітуда')
plt.legend()
plt.grid()
plt.show()

print("--------------------------\nДискретні відліки сигналу:\n--------------------------\n")
for i, val in enumerate(x_discrete):
    print(f"x{i + 1} = {val:.8f}")

# Відносна похибка для прикладу (t = 0.15)
t_example = 0.15
x_analog_example = A * np.cos(omega * t_example + phi)
x_reconstructed_example = np.sum([x_discrete[k] * np.sinc(np.pi * (t_example / Td - k)) for k in range(K)])
error = np.abs((x_analog_example - x_reconstructed_example) / x_analog_example) * 100

print(f"\n--------------------------\nВідносна похибка відновлення\n--------------------------\nt = {t_example} с: {error:.2f}%")
