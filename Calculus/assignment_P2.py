from sympy import *
import numpy as np 
import matplotlib.pyplot as plt
import random

def requirement1():
    t = np.arange(-np.pi, np.pi,0.01)
    xh = 4*np.sin(t)**5 + 5
    yh = 3*np.cos(t) - 1.7*np.cos(2*t) - np.cos(3*t) + 1
    return xh,yh

def requirement2(ID, n,d,a,a0,x,y):
    x_new, y_new = x,y
    I = "F+F+F+F+F+F+F+F"
    index = 0
    while index != n:
        I = I.replace("F", "F---F+F+F+F+F+F+F---F")
        index+=1
    Pxn = []
    Pyn = []
    for i in I:
        if i == 'F':
            x_new -= d*cos(a*pi/180)
            y_new += d*sin(a*pi/180)
            Pxn.append(x_new)
            Pyn.append(y_new)
        if i == '+':
            a = a+a0
        if i == '-':
            a = a-a0
    return Pxn, Pyn

def requirement3(ID,n,d,a,a0,x,y):
    x_new,y_new = x,y
    I = "FX"
    index = 0
    Px = [-10]
    Py = [-10]
    while index != n:
        I = I.replace("F", "FF")
        I = I.replace("X", "F[+X][-X]FXo")
        index+=1

    D = []
    A = []
    P = []
    for i in I:
        if i == 'F':
            x_new -= d*cos(a*np.pi/180)
            y_new += d*sin(a*np.pi/180)
            Px.append(x_new)
            Py.append(y_new)
        if i == '+':
            a = a+a0
        if i == '-':
            a = a-a0
        if i == '[':
            D.append(d)
            A.append(a)
            P.append(x_new)
            P.append(y_new)
        if i == ']':
            a = A.pop()
            d = D.pop()
            y_new = P.pop()
            x_new = P.pop()
            Py.append(y_new)
            Px.append(x_new)
    return Px, Py

def requirement4(ID,n,d,a,a0,x,y):
    x_new,y_new = x,y
    I = "FX"
    index = 0
    Px = []
    Py = []
    while index != n:
        I = I.replace("F", "FF")
        I = I.replace("X", "F[+X][-X]FXo")
        
        index+=1

    D = []
    A = []
    P = []
    Pfx = []
    Pfy = []

    for i in I:
        if i == 'F':
            x_new -= d*cos(a*pi/180)
            y_new += d*sin(a*pi/180)
            Px.append(x_new)
            Py.append(y_new)
        if i == '+':
            a = a+a0
        if i == '-':
            a = a-a0
        if i == '[':
            D.append(d)
            A.append(a)
            P.append(x_new)
            P.append(y_new)
        if i == ']':
            a = A.pop()
            d = D.pop()
            y_new = P.pop()
            x_new = P.pop()
            Py.append(y_new)
            Px.append(x_new)
        if i == 'o':
            Pfx.append(x_new)
            Pfy.append(y_new)

    return Pfx, Pfy

def requirement5(d1,d2):
    x = symbols('x')
    nfw = (integrate(x/2, (x,min(d1,d2), max(d1,d2))) + 1) % 3 + 1
    return nfw

def requirement6(d1,d2):
    phi = 0
    
    k = (d2+1)/(d1+1) if (d2+1)%(d1+1) != 0 else (d2+1)/(d1+2)
    x_fw = [cos(k*phi)*cos(phi)*15]
    y_fw = [cos(k*phi)*sin(phi)*15]
    while phi <= 4*np.pi:
        phi = phi + 1/(2*np.pi)
        x_fw.append(cos(k*phi)*cos(phi)*15)
        y_fw.append(cos(k*phi)*sin(phi)*15)
    
    return x_fw, y_fw

def requirement7(d1):
    x = symbols('x')
    f = x**2 - d1*x + 1
    nsnowflake = solve(diff(f,x,1))
    return nsnowflake[0]

def requirement8(xt,yt, scale,d1,d2):
    ax = plt.axes()
    ax.set_facecolor("black")
    #a)
    plt.text(xt, yt, 'Happy New Year 2022', fontsize = 12,color='w')
    #b)
    Pxn, Pyn = requirement2(5,2,5,0,45,0,0)
    for i in range(0,requirement7(d1)):
        delta_x = random.randint(-10,100)
        delta_y = random.randint(50,100)
        x_new = []
        y_new = []
        for k,h in zip(Pxn,Pyn):
            x_new.append(k/scale + delta_x)
            y_new.append(h/scale + delta_y)
        plt.plot(x_new, y_new, color = 'w', linewidth=1)
    #c)
    plt.plot(requirement3(2,3,10,90,25,-10,-10)[0], requirement3(2,3,10,90,25,-10,-10)[1], color='green', linewidth= 2)
    plt.plot(requirement4(2,3,10,90,25,-10,-10)[0], requirement4(2,3,10,90,25,-10,-10)[1],'+',linewidth=3)
    #d)
    delta_x = random.randint(100,250)
    delta_y = random.randint(100,300)
    Pxn, Pyn = requirement6(d1,d2)
    x_new, y_new = [], []
    for i in range(0,requirement5(d1,d2)):
        for k,h in zip(Pxn,Pyn):
            x_new.append(5*k + delta_x)
            y_new.append(5*h + delta_y)
        for j in range(0, len(x_new)):
            if j % 4 == 0:
                s = 'r*'
            elif j % 4 == 2:
                s = 'm+'
            else:
                s = 'c*'
            plt.plot(x_new[j], y_new[j], s)
    #e)
    xh, yh = requirement1()
    x_new, y_new = [], []
    for i,j in zip(xh,yh):
        x_new.append(2*i+xt-20)
        y_new.append(2*j)
    plt.fill(x_new, y_new, 'r')
    plt.show()



xt = 50
yt = 0
scale = 15
d1,d2 = 4, 4
requirement8(xt, yt,scale,d1,d2)