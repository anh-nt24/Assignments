from sympy import * ## KHONG XOA
import numpy as np ## KHONG XOA 

global x, y, z, t ## KHONG XOA
x, y, z, t = symbols("x, y, z, t") ## KHONG XOA     

def req1(f, g, a):  ## KHONG XOA
    if (type(f)==int or type(f)==float) and (type(g)==int or type(g)==float):
        A=[0.0,0.0,0.0]
        try:
            f/g
            A.append(0.0)
        except:
            A.append(None)
        A=tuple(A)
        return A
    A=[f+g,f*g,f,f]
    for i in range (len(A)):
        try:
            if i==2:
                A[i]=f.subs(x,g)
            if i==3:
                A[i]=f/g
            dx=diff(A[i],x,1).subs(x,a)
            if (type(dx) != float or type(dx) != int):
                try:
                    float(dx)
                    R = limit((A[i]-A[i].subs(x,a))/(x-a),x,a,'+')
                    L = limit((A[i]-A[i].subs(x,a))/(x-a),x,a,'-')
                    if str(abs(round(dx))).isnumeric()==False:
                        if L==R and str(abs(round(L))).isnumeric()==False:
                            A[i]=None
                        elif L==R and str(abs(round(L))).isnumeric()==True:
                            A[i]=round(float(L),2)
                        else:
                            A[i]=None
                    else:
                        A[i]=round(float(dx),2)
                except:
                    R = limit((A[i]-A[i].subs(x,a))/(x-a),x,a,'+')
                    L = limit((A[i]-A[i].subs(x,a))/(x-a),x,a,'-')
                    if str(abs(round(R))).isnumeric()==False or R!=L:
                        A[i]=None
                    else:
                        A[i]=round(float(R),2)
            else:
                A[i]=round(float(dx),2)
        except:
            if i==2 and (type(f)==int or type(f)==float):
                A[i]=0.0
            else:
                A[i]=None
    A=tuple(A)
    return A


def req2(f, a, b, c):  ## KHONG XOA
    if type(f)==int or type(f)==float:
        return f
    L1=limit(limit(limit(f,x,a),y,b),z,c)
    L2=limit(limit(limit(f,x,a),z,c),y,b)
    L3=limit(limit(limit(f,y,b),x,a),z,c)
    L4=limit(limit(limit(f,y,b),z,c),x,a)
    L5=limit(limit(limit(f,z,c),y,b),x,a)
    L6=limit(limit(limit(f,z,c),x,a),y,b)
    if L1 == L2 == L3 == L4 == L5 == L6:
        mx_a=diff(f,x,1).subs({x:a,y:b,z:c})
        my_b=diff(f,y,1).subs({x:a,y:b,z:c})
        mz_c=diff(f,z,1).subs({x:a,y:b,z:c})
        try:
            float(L1)
            float(mx_a)
            float(my_b)
            float(mz_c)
            tg=mx_a*(x-a) + my_b*(y-b) + mz_c*(z-c) + f.subs({x:a,y:b,z:c})
            if "nan" in str(tg) or "oo" in str(tg):
                tg=None
        except:
            return None
    return tg

def req3(w, f1, f2, f3, a):  ## KHONG XOA
    if type(w)==int or type(w)==float:
        return 0.0
    wxt=w.subs({x:f1, y:f2, z:f3})
    try:
        dw=diff(wxt,t,1).subs(t,a).evalf()
        if str(abs(round(dw))).isnumeric() == True:
            return round(float(dw),2)
    except:
        try:
            R = limit((wxt-wxt.subs(t,a))/(t-a),t,a,'+')
            str(abs(round(R))).isnumeric()
            L = limit((wxt-wxt.subs(t,a))/(t-a),t,a,'-')
            str(abs(round(L))).isnumeric()
            if L==R:
                return round(float(L),2)
            else:
                return None
        except:
            None



def req4(a, b, n):  ## KHONG XOA
    newton=0
    for k in range(n+1):
        Choose=float(factorial(n)/(factorial(k)*factorial(n-k)))
        newton=newton+Choose*(a**(k))*(b**(n-k))
    return newton



def req5(f):  ## KHONG XOA
    zx=diff(f,x,1)
    zy=diff(f,y,1) 
    n=solve([zx,zy],(x,y))
    fxx=diff(zx,x,1)
    fxy=diff(zx,y,1)
    fyy=diff(zy,y,1)
    delta=fxx*fyy - fxy**2
    CD=[]
    CT=[]
    SP=[]
    if (type(n)!=list):
        X=n[x]
        Y=n[y]
        n=[]
        n.append((X,Y))
    for i in n:
        d=delta.subs({x:i[0], y:i[1]})
        A=fxx.subs({x:i[0], y:i[1]})
        try:
            if d>0 and A>0 and i[0] != I and i[1] !=I and i[0]!= -I and i[1] != -I:
                CT.append((i[0],i[1]))
            if d>0 and A<0 and i[0] != I and i[1] !=I and i[0]!= -I and i[1] != -I:
                CD.append((i[0],i[1]))
            if d<0:
                SP.append((i[0],i[1]))
            if d==0:
                delta_x1=i[0] + 10**(-9)
                delta_y1=i[1] + 10**(-9)
                delta_x2=i[0] - 10**(-9)
                delta_y2=i[1] - 10**(-9)
                df1=f.subs({x: delta_x1, y: delta_y1}) - f.subs({x:i[0], y:i[1]})
                df2=f.subs({x: delta_x2, y: delta_y2}) - f.subs({x:i[0], y:i[1]})
                if df1>0 and df2>0:
                    CT.append((i[0],i[1]))
                elif df1<0 and df2<0:
                    CD.append((i[0],i[1]))
        except:
            continue
    return CT


def req6(message, x, y, z):  ## KHONG XOA
    key='{0:08b}'.format(abs(x**2 - y**2 - z))
    text=''
    for i in message:
        cypher="{0:08b}".format(ord(i))
        c=0
        plain=''
        for c in range(len(cypher)):
            if cypher[c]==key[c]:
                plain+='0'
            else:
                plain+='1'
        text+=chr(int(plain,2))
    return text


def req7(xp, yp, xc):  ## KHONG XOA
    n=len(xp)
    a=0
    b=0
    c=0
    d=0
    for i in range (n):
        a=a+xp[i]
        b=b+yp[i]
        c=c+xp[i]*yp[i]
        d=d+(xp[i])**2
    m= (a*b - n*c)/((a**2) - n*d)
    b=(1/n)*(b - m*a)
    y=round(float((m*x + b).subs(x,xc)),2)
    return y



def req8(f, eta, xi, tol): ## KHONG XOA
    t=xi
    dx=diff(f,x,1)
    try:
        increasing = solveset(dx>0, x, S.Reals)
        decreasing = solveset(dx<0, x, S.Reals)
        if increasing == Interval(-oo, oo) or decreasing == Interval(-oo, oo):
            return None
        if decreasing == Interval.open(0, oo):
            return None
        if decreasing == Union(Interval.open(-oo, 0), Interval.open(0, oo)) and increasing == EmptySet:
            return None
    except:
        pass
    try:    
        if int(diff(dx,x,1)) <= 0:  
            return None  
    except:
        try:
            a = solve(diff(f,x,2))
            if a == []:
                return None 
        except:
            pass
    while True:
        t = (t - eta*dx.subs(x,t)).evalf()
        if abs(dx.subs(x,t)) < tol:
            break
    return float("{:0.2f}".format(round(t,2)))
print(type(1/3))