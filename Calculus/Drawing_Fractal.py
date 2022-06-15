import matplotlib.pyplot as plt
from math import *

#a)
print('a)')
Fa="F+F-F-F+F"
f0=Fa
a=0
d=2
t=90
n=5

Fa_new=Fa
while n>0:
  Fa_new=Fa.replace("F",f0)
  Fa=Fa_new
  n=n-1

Px=[0]
Py=[0]
x_new=0
y_new=0
for i in Fa:
  if i=="F":
    x_new=x_new - d*cos(a*pi/180)
    y_new=y_new + d*sin(a*pi/180)
    Px.append(x_new)
    Py.append(y_new)
  elif i=="-":
    a=a-t
  elif i=='+':
    a=a+t

fig=plt.figure()
plt.plot(Px,Py)
plt.show()


#b)
print('b)')
Fb="F[+F][-F]"
f1=Fb
a=90
d=2
t=45
n=10

Fb_new=Fb
while n>0:
  Fb_new=Fb.replace("F",f1)
  Fb=Fb_new
  n=n-1

Qx=[0]
Qy=[0]
x_new=0
y_new=0
S=[]
A=[]
D=[]
for i in Fb:
  if i=="F":
    x_new=x_new - d*cos(a*pi/180)
    y_new=y_new + d*sin(a*pi/180)
    Qx.append(x_new)
    Qy.append(y_new)
    d=d*0.5
  elif i=='-':
    a=a-t
  elif i=='+':
    a=a+t
  elif i=='[':
    A.append(a)
    D.append(d)
    S.append(x_new)
    S.append(y_new)
  elif i==']':
    a=A.pop()
    d=D.pop()
    y_new=S.pop()
    x_new=S.pop()
    Qx.append(x_new)
    Qy.append(y_new)
    
fig=plt.figure()
plt.plot(Qx,Qy)
plt.show()
