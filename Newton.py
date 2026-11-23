#Importamos os módulos e os comandos de Python necesarios:
import numpy as np
import sympy as sp
from sympy import Symbol,Derivative,simplify,lambdify
import matplotlib.pyplot as plt

#Definimos a función cuxas raíces queremos aproximar (cada grupo usará unha función distinta):

z=Symbol('z')
f=z/(z**2+z)**(1/2)


#Definimos a derivada da función anterior. Se fose necesario para algún método
#definiríase de forma similar a segunda derivada.

derf=Derivative(f,z,1).doit()

#Definimos a fórmula do método que queremos implementar. Neste exemplo 
#tratase do Método de Newton. Para implementar outro metodo debemos definir 
# a fórmula correspondente:

#Metodo de Newton
g=simplify(z-f/derf)

# Os seguintes parámetros poden ser modificados co obxetivo de 
#conseguir os mellores gráficos posibles: 

# Número máximo de iteracións para o método elexido:

maxiter=30

#O fractal representarase no rectángulo [a,b]x[c,d]: 

a=-1.1
b=0.6
c=-0.5
d=0.5

#Número de puntos usados nos eixos OX e OY para representar o fractal: canto
#maior sexa o número de puntos máis preciso sera o gráfico, pero tamén máis
#tempo se necesitará para levar a cabo os cálculos.

npuntos=300

################### NON MODIFICAR ESTA PARTE DO PROGRAMA #####################
##############################################################################

ff=lambdify(z,f,"numpy")
gg=lambdify(z,g,"numpy")
fractal = np.zeros((npuntos+1,npuntos+1))
tol=1.0e-6

x=np.linspace(a,b,npuntos+1)
y=np.linspace(c,d,npuntos+1)

for i in range(0,npuntos):
    for j in range(0,npuntos):
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
print('MÉTODO DE NEWTON')       
print('A función utilizada é: f(z)=',f)
print('A súa derivada é: derf(z)=',derf)
print('A función do método de Newton é: g(z)=',g)

#A continuación represéntase a imaxen fractal: recoméndase buscar unha gama de 
#cores atractiva. 

plt.imshow(fractal,cmap='coolwarm', extent=(a, b, c, d))
plt.colorbar()
plt.xlabel("x")
plt.ylabel("y")

#A continuación gárdase a imaxen do fractal nun ficheiro: cambiar o nome do 
#ficheiro según o método usado 

plt.savefig('fractal_Newton.png', dpi=2000)
plt.show()