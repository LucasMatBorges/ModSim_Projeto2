from scipy.integrate import odeint
from numpy import linspace
import matplotlib.pyplot as plt


A0 = 296.0   # Temperatura inicial da água (Kelvin)
Tinf = 281.0 # Temperatura do ambiente (geladeira) (Kelvin)

Ma = 1.585    # Massa da água (kilograma)
Ca = 4181.3  # Calor específico da água (J/(kg*K))

Kr = 0.195   # Coeficiente de condutividade térmica - RECIPIENTE. (W/(m*K))
H = 7.746616415892147     # Coeficiente da troca de calor por convecção - AR. (W/(m**2*K))
 
Ar = 0.085   # Superfície de contato do recipiente (m**2)
Lr = 0.001   # Espessura do recipiente (m)


"""Equações diferenciais
   Calcula variação de temperatura dos estoques"""
def func(A, t):
    dAdt = ( (Tinf - A) / (Ma*Ca) ) * ( (H*Kr*Ar) / ( (H*Lr) + Kr) )# * ( ( (H*Lr) + Kr) / (H*Lr) )
    return dAdt

T = linspace(0,60000,60001)


Y = odeint(func, A0, T)
#k = 0.023/Dh = 2*(A/P) = 2*( 0.1558/1.58 ) = 0.1972151898734177 / Nu = 0.023 * 0.7**0.4 * 3000**0.8 = 12.063242431442934

TempsG = [294.7,293.8,291, 287,284.2,284.4,283.7,283.6]
TG = [900,1500,5000,9000,17100,18000,18900,19800]

"""Gráfico da variação de temperatura da água por tempo"""
plt.title("Temperatura da Água")
plt.plot(TG, TempsG, 'bo')
plt.plot(T, Y, "g")
plt.axis([0,max(T),280,300])
plt.ylabel('Temperatura (K)')
plt.xlabel('Tempo (s)')
plt.show()




# Gráfico matador






import matplotlib.pyplot as plt
from scipy.integrate import odeint 
from numpy import linspace





A0 = 296.0   # Temperatura inicial da água (Kelvin)
Tinf = 281.0 # Temperatura do ambiente (geladeira) (Kelvin)

Ma = 1.585    # Massa da água (kilograma)
Ca = 4181.3  # Calor específico da água (J/(kg*K))

Kr = 0.195   # Coeficiente de condutividade térmica - RECIPIENTE. (W/(m*K))
H = 7.746616415892147     # Coeficiente da troca de calor por convecção - AR. (W/(m**2*K))
 
Ar = 0.085   # Superfície de contato do recipiente (m**2)
Lr = 0.001   # Espessura do recipiente (m)

"""Equações diferenciais
   Calcula variação de temperatura dos estoques"""
def func(Y, t):
    Ar = Y[1]
    dAdt = ( (Tinf - Y[0]) / (Ma*Ca) ) * ( (H*Kr*Ar) / ( (H*Lr) + Kr) )
    return dAdt

T = linspace(0,100000,100001)
Y0 = [A0]
Ar0lista = linspace(0,1,1001)


def calculaTemperatura(Ar0, T):
    Y0.append(Ar0)
    Y = odeint(func, Y0, T)
    Y0.pop()
    return Y[:,0]

def determinaTempoMenorX(C, T, x):
    idx = 0
    n = len(C)
    achou = 0
    while achou == 0 and idx < n-1:
        if (C[idx+1] < x and C[idx] > x):
            achou = 1
        idx += 1
    if idx == n-1:
        idx = 0
    return T[idx]

def calculaTempoMenorX(Ar0lista, T, x):
    TempoMenorXLista = []
    for ar0 in Ar0lista:
        C = calculaTemperatura(ar0, T)
        TempoMenorX = determinaTempoMenorX(C, T, x)
        TempoMenorXLista += [TempoMenorX]
    return TempoMenorXLista


TempoMenorXLista = calculaTempoMenorX(Ar0lista, T, 281.2)

plt.title('Tempo de resfriamento em função da superfície de contato')
plt.plot(Ar0lista, TempoMenorXLista, 'k')
plt.xlabel('Superfície de contato (m²)')
plt.ylabel('Tempo de Resfriamento (s)')
plt.show()
