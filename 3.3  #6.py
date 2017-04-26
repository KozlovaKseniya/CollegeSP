import math
n=int(input('Введите n - '))
s=float(1)
x=float(input('x = '))
for i in range(1,n+1):
    s=s+math.cos(i*math.pi/4)/math.factorial(i)*math.pow(x,i)
print('S = ',s)
