import numpy as np
import matplotlib.pyplot as plt
a = 0.1382
b = 3.19*10**(-5)
R = 8.314
T_crit = (8*a)/(27*R*b)
def vdw_pressure(V, T, a, b, R):
    return (R * T / (V - b)) - (a / V ** 2)
def C_to_K(T_C):
    return T_C + 273.15
temperature_C = [-100, -110, -120, -130, -140]
temperature_K = [C_to_K(T) for T in temperature_C]
V = np.linspace(b + 10**(-5), 10**(-3), 5000)
plt.figure(figsize=(12, 8))
plt.xlabel('Объем, м^3/моль')
plt.ylabel('Давление, Па')
plt.title('Изотермы Ван-дер-Ваальса для воздуха')
m=0
for T_C, T_K in zip(temperature_C, temperature_K):
    P = vdw_pressure(V, T_K, a, b, R)
    if T_K>T_crit and m==0:
        plt.plot(V, P, label=f'{T_C}°C', color='red')
        m+=1
    else:
        plt.plot(V, P, label=f'{T_C}°C', color='blue')
plt.xscale('log')
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show()