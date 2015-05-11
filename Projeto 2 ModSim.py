from scipy.integrate import odeint
from numpy import linspace
import matplotlib.pyplot as plt


A0 = 298.0   # Temperatura inicial da água (Kelvin)
Tinf = 283.0 # Temperatura do ambiente (geladeira) (Kelvin)

Ma = 1.5     # Massa da água (kilograma)
Ca = 4181.3  # Calor específico da água (J/(kg*K))

Kr = 0.195   # Coeficiente de condutividade térmica - RECIPIENTE. (W/(m*K))
H = 7.746616415892147     # Coeficiente da troca de calor por convecção - AR. (W/(m**2*K))
 
Ar = 0.085   # Superfície de contato do recipiente (m**2)
Lr = 0.001   # Espessura do recipiente (m)

"""Equações diferenciais
   Calcula variação de temperatura dos estoques"""
def func(A, t):
    dAdt = ( (Tinf - A) / (Ma*Ca) ) * ( (H*Kr*Ar) / ( (H*Lr) + Kr) ) * ( ( (H*Lr) + Kr) / (H*Lr) )
    return dAdt

T = linspace(0,3600,3601)


Y = odeint(func, A0, T)
#k = 0.023/Dh = 0.1421 / Nu = 0.023 * 0.7**0.4 * 2000**8

"""Gráfico da variação de temperatura da água por tempo"""
plt.title("Temperatura da Água")
plt.plot(T, Y, "g")
plt.axis([0,max(T),280,300])
plt.ylabel('Temperatura (K)')
plt.xlabel('Tempo (s)')
plt.show()
