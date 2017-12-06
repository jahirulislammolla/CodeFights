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
    
