# ''''
# Use the determinant:
# | x_1^2 x_1*y_1 y_1^2 x_1 y_1 1 |
# | x_2^2 x_2*y_2 y_2^2 x_2 y_2 1 |
# | x_3^2 x_3*y_3 y_3^2 x_3 y_3 1 |
# | x_4^2 x_4*y_4 y_4^2 x_4 y_4 1 |
# | x_5^2 x_5*y_5 y_5^2 x_5 y_5 1 |
# |  x^2    x*y    y^2   x   y  1 |
# to solve for the coefficients in
# Ax^2 + Bxy + Cy^2 + Dx + Ey + F = 0        
# ''''
#|  A  B/2 D/2 |
#| B/2  C  E/2 |
#| D/2 E/2  F  |
# 
#https://math.stackexchange.com/questions/163920/how-to-find-an-ellipse-given-five-points
#https://math.stackexchange.com/questions/247332/area-of-an-ellipse
#import numpy as np
#def ellipticSystem(points):
#
#    M = np.array([ [x*x,x*y,y*y,x,y,1.] for x,y in zip(points[::2],points[1::2])])
#    A,B,C,D,E,F =  [np.linalg.det(M[:,[ i!=k for i in range(6)]])*(-1)**k for k in range(6)]
#    I1= A+C
#    I2= (A-C)**2+B*B
#    I3= D*D+E*E
#    I4= (A-C)*(D*D-E*E)+2*D*E*B
#    I5 = F
#    return abs(np.pi*(I1*I3-I4-2*(I1**2-I2)*I5)/(I1**2-I2)**1.5)
from itertools import permutations
import math
def sin(check):
    s=0
    for i in range(6):
        for j in range(i):
            if check[i]<check[j]:
                s+=1
    return 1-2*(s%2)
def ellipticSystem(points):
    m=[]
    for i in range(0,len(points),2):
        x,y=points[i],points[i+1]
        m+=[[x*x,x*y,y*y,x,y,1]]
    c=[0,0,0,0,0,0]
    x=[0,1,2,3,4,5]
    for i in permutations(x):
        p=sin(i)
        for j in range(5):
            p*=m[j][i[j]]
        c[i[5]]+=p
    A,B,C,D,E,F=c[0],c[1],c[2],c[3],c[4],c[5]
    dis = B*B - 4*A*C
    det = A*C*F + B*D*E/4.0 - A*E*E/4.0 - B*B*F/4.0 - C*D*D/4.0
    a = 2*math.sqrt(2*det/dis/((A+C)-math.sqrt((A-C)*(A-C)+B*B)))
    b = 2*math.sqrt(2*det/dis/((A+C)+math.sqrt((A-C)*(A-C)+B*B)))
    return math.pi*a*b

#same code.... 

import numpy as n
A,B,C,D,E = n.linalg.solve([[x*x,x*y,y*y,x,y] for x,y in zip(*[iter(eval(dir()[0])[0])]*2)],[1]*5)
i= 4*A*C-B*B
return n.pi*2*abs(A*E*E+C*D*D-D*E*B+i)/i**1.5
    
#same code.....

from numpy import *
a,b,c,d,f=linalg.inv([(x*x,x*y,y*y,x,y) for x,y in reshape(eval(dir()[47]),(5,2))]).dot([1]*5)
q=4*a*c-b*b
return pi*abs(q+a*f*f+c*d*d-b*d*f)/q**1.5*2
    
