#Marco Aldair De Jesus Caceres
#Numero de control 18390579
#14/12/2020
#Examen
import matplotlib.pyplot as plt
import numpy as np
#Colocamos los ejes del plano
plt.axis([-150,350,300,-100])
plt.axis('on')
plt.grid(True)

#Creamos la variable del color RGB
c = (.5,.7,.9)
#Establecemos el centro del circulo y el radio
xc = 100
yc = 100
r = 45
#Punto de inicio del circulo
p1 = 0 * np.pi/180
#Punto de termino del circulo
p2 = 360 * np.pi/180
dp = (p2-p1)/100

xlast = xc + r * np.cos(p1)
ylast = yc + r * np.sin(p1)

#Este ciclo es el encargado de dibujar el circulo
for p in np.arange(p1,p2+dp,dp):
    xp = xc + r * np.cos(p)
    yp = yc + r * np.sin(p)
    plt.plot([xlast,xp],[ylast,yp],color = c,linewidth = 1)
    xlast = xp
    ylast = yp

#Declaramos las variables del escalado
rz = 42
sx = 1.8
sy = 1.4

#Creamos un nuevo centro para el primer rectangulo
rxc = 55
ryc = 55
#En estos arrays almacenaremos las coordenadas del primer rectangulo
xr = np.array([rxc,rxc,rxc + 2*r,rxc + 2*r,rxc])
yr = np.array([ryc,ryc + 2*r,ryc + 2*r,ryc,ryc])
#En este array se almacena las coordenadas del rectangulo escalado
x=np.array([xc,xc,(xc+2*r) * sx,(xc+2*r)*sx,xc])
y=np.array([yc,(yc+2*r) * sy,(yc+2*r) * sy,yc,yc])
#Con esta instruccion imprimimos los rectangulos
plt.plot(xr,yr, color = c)
plt.plot(x,y, color=c)

plt.axes().set_aspect('equal')
plt.show()
