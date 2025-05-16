import numpy as np
import matplotlib.pyplot as plt

h = 6.62607015e-34     # Планка, Дж·с
c = 2.99792458e8       # скорость света, м/с
me = 9.10938356e-31    # масса электрона, кг
compton_const = h / (me * c)  # Постоянная Комптона (в м)

lambda0_nm = float(input("Введите исходную длину волны (в нанометрах): "))
theta_deg_input = float(input("Введите угол рассеяния (в градусах): "))

# Перевод в метры и радианы
lambda0 = lambda0_nm * 1e-9
theta_rad_input = np.deg2rad(theta_deg_input)

# Расчёт изменения длины волны и новых значений
delta_lambda_input = compton_const * (1 - np.cos(theta_rad_input))
lambda1 = lambda0 + delta_lambda_input

# Энергии фотонов
E0 = h * c / lambda0
E1 = h * c / lambda1

print("\nРезультаты")
print(f"Исходная длина волны: {lambda0_nm:.4f} нм")
print(f"Угол рассеяния: {theta_deg_input:.2f}°")
print(f"Изменение длины волны: {delta_lambda_input*1e12:.4f} пм")
print(f"Длина волны после рассеяния: {lambda1*1e9:.4f} нм")
print(f"Энергия до: {E0 / 1.602e-19:.4f} эВ")
print(f"Энергия после: {E1 / 1.602e-19:.4f} эВ")


#Построение графика зависимости изменения волны от угла
theta_deg = np.linspace(0, 180, 500)
theta_rad = np.deg2rad(theta_deg)
delta_lambda = compton_const * (1 - np.cos(theta_rad))

plt.figure(figsize=(8, 5))
plt.plot(theta_deg, delta_lambda * 1e12, label='Δλ (пм)')
plt.axvline(theta_deg_input, color='red', linestyle='--', label='Указанный угол')
plt.axhline(delta_lambda_input * 1e12, color='green', linestyle='--', label='Δλ при этом угле')

plt.title("Эффект Комптона: изменение длины волны от угла")
plt.xlabel("Угол рассеяния (°)")
plt.ylabel("Изменение длины волны Δλ (пм)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
