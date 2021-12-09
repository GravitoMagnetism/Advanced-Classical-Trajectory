import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

gamma=1
beta=1
m=1
g=9.81

t = np.linspace(0, 10, 101)

def dv_x_dt(v_x,v_y):
    print(v_x,v_y)
    return -(gamma*v_x)-(beta*(v_x**2))-(beta*(v_y**2))

def dv_y_dt(v_x,v_y):
    return -(gamma*v_y)-(beta*(v_x**2))-(beta*(v_y**2))-(m*g)

def dx_dt(v_x):
    return v_x

def dy_dt(v_y):
    return v_y

def traj(t):
    x=0
    y=0
    theta=np.pi/2
    v_x=1*np.sin(theta)
    v_y=1*np.cos(theta)
    dt=0.01
    plot=[]
    for time in np.arange(0,t,dt):
        a_x=dv_x_dt(v_x,v_y)
        a_y=dv_y_dt(v_x,v_y)
        x+=v_x*dt
        y+=v_y*dt
        v_x+=a_x*dt
        v_y+=a_y*dt
        plot.append([x,y])
    return plot

t=10

plt.plot(traj(t)[0],traj(t)[1])
plt.legend(loc='best')
plt.xlabel('x')
plt.xlabel('y')
plt.grid()
plt.show()