#Importamos os módulos e os comandos de Python necesarios:
import numpy as np
import sympy as sp
from sympy import Symbol,Derivative,simplify,lambdify
import matplotlib.pyplot as plt
import os

#Definimos a función cuxas raíces queremos aproximar (cada grupo usará unha función distinta):

z=Symbol('z')
f=z**3-2*z+2

#Definimos a derivada da función anterior e a segunda derivada, necesaria para Halley:

derf=Derivative(f,z,1).doit()
derf2=Derivative(f,z,2).doit()

#Metodo de Halley:
#x_{n+1} = x_n - 2*f(x_n)*f'(x_n) / (2*f'(x_n)^2 - f(x_n)*f''(x_n))
#Expresado como punto fixo g(z) para poder reutilizar o bucle de Newton:

g=simplify(z - (2*f*derf)/(2*derf**2 - f*derf2))

# Os seguintes parámetros poden ser modificados co obxetivo de
#conseguir os mellores gráficos posibles:

maxiter=30

#O fractal representarase no rectángulo [a,b]x[c,d]:

a=-2.0
b=2.0
c=-2.0
d=2.0

#Número de puntos usados nos eixos OX e OY para representar o fractal:

npuntos=600

################### NON MODIFICAR ESTA PARTE DO PROGRAMA #####################
##############################################################################

ff=lambdify(z,f,"numpy")
gg=lambdify(z,g,"numpy")
fractal = np.zeros((npuntos+1,npuntos+1))
tol=1.0e-6

x=np.linspace(a,b,npuntos+1)
y=np.linspace(c,d,npuntos+1)

for i in range(0,npuntos+1):
    for j in range(0,npuntos+1):
        z = complex(x[i],y[j])
        n=0
        while (n<maxiter and abs(ff(z))>tol):
            if abs(gg(z))<1/tol:
               z=gg(z)
               n=n+1
            else:
               break
        fractal[npuntos-j,i]=float(n)

##############################################################################
##############################################################################

print('')
print('MÉTODO DE HALLEY')
print('A función utilizada é: f(z)=',f)
print('A súa derivada é: derf(z)=',derf)
print('A segunda derivada é: derf2(z)=',derf2)
print('A función do método de Halley é: g(z)=',g)

plt.figure(figsize=(9, 6))
plt.imshow(fractal,cmap='turbo', extent=(a, b, c, d))
plt.colorbar(label='iteracións')
plt.xlabel("Re(z)")
plt.ylabel("Im(z)")

os.makedirs('imaxes', exist_ok=True)
plt.savefig('imaxes/fractal_Halley.png', dpi=300, bbox_inches='tight')
plt.close()
