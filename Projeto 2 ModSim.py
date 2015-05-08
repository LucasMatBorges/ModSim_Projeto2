from scipy.integrate import odeint
from numpy import linspace
import matplotlib.pyplot as plt


A0 = 298.0   # Temperatura inicial da água (Kelvin)
R0 = 298.0   # Temperatura inicial do recipiente (Kelvin)
Tinf = 283.0 # Temperatura do ambiente (geladeira) (Kelvin)

Ma = 1.5     # Massa da água (kilograma)
Ca = 4181.3  # Calor específico da água (J/(kg*K))
Mr = 0.2     # Massa do recipiente (kilograma)
Cr = 1000.0  # Calor específico da água (J/(kg*K))

Kr = 0.195   # Coeficiente de condutividade térmica - RECIPIENTE. (W/(m*K))
H = 0.4      # Coeficiente da troca de calor por convecção - AR. (W/(m**2*K))
 
Ar = 0.085   # Superfície de contato do recipiente (m**2)
Lr = 0.001   # Espessura do recipiente (m)

"""Equações diferenciais
   Calcula variação de temperatura dos estoques"""
def func(Y, t):
    dAdt = ( (Kr*Ar) / (Ma*Ca*Lr) ) * (Tinf - Y[0])
    dRdt = ( Ar / (Mr*Cr) ) * ( ( ( Kr*(Y[0] - Y[1]) ) / Lr ) - ( H*(Y[1] - Tinf) ) )
    return [dAdt, dRdt]

T = linspace(0,3600,3601)
Y0 = [A0, R0]


Y = odeint(func, Y0, T)


"""Gráfico da variação de temperatura da água por tempo"""
plt.title("Temperatura da Água")
plt.plot(T, Y[:,0], "g")
plt.axis([0,max(T),280,300])
plt.ylabel('Temperatura (K)')
plt.xlabel('Tempo (s)')
plt.show()

"""Gráfico da variação de temperatura do recipiente por tempo"""
plt.title("Temperatura do recipiente")
plt.plot(T, Y[:,1])
plt.axis([0,max(T),280,300])
plt.ylabel('Temperatura (K)')
plt.xlabel('Tempo (s)')
plt.show()

Text = 'Água','Recipiente'

"""Junção da variação de temperatura da água e do recipiente em 60s"""
plt.title("Comportamento inicial do sistema")
plt.plot(T,Y[:,0])
plt.plot(T,Y[:,1])
plt.axis([0,60,296,298.5])
plt.legend(Text,bbox_to_anchor=(1.0, -0.15),ncol=2,fancybox=True, shadow=True)
plt.ylabel('Temperatura (K)')
plt.xlabel('Tempo (s)')
plt.show()