#Marco Aldair De Jesus Caceres
#Examen
import matplotlib.pyplot as plt
import numpy as np
plt.axis([-150,350,300,-100])
plt.axis('on')
plt.grid(True)

c = (.5,.7,.9)
xc = 100
yc = 100
r = 45
p1 = 0 * np.pi/180
p2 = 360 * np.pi/180
dp = (p2-p1)/100

xlast = xc + r * np.cos(p1)
ylast = yc + r * np.sin(p1)

for p in np.arange(p1,p2+dp,dp):
    xp = xc + r * np.cos(p)
    yp = yc + r * np.sin(p)
    plt.plot([xlast,xp],[ylast,yp],color = c,linewidth = 1)
    xlast = xp
    ylast = yp

#x1 = 20
#y1 = 50
#x2 = 200
#y2 = 50

rz = 42
sx = 1.8
sy = 1.4

rxc = 55
ryc = 55




xr = np.array([rxc,rxc,rxc + 2*r,rxc + 2*r,rxc])
yr = np.array([ryc,ryc + 2*r,ryc + 2*r,ryc,ryc])

x=np.array([xc,xc,(xc+2*r) * sx,(xc+2*r)*sx,xc])
y=np.array([yc,(yc+2*r) * sy,(yc+2*r) * sy,yc,yc])

plt.plot(xr,yr, color = c)
plt.plot(x,y, color=c)


plt.axes().set_aspect('equal')
plt.show()