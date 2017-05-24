import array
import math
n=int(12)
Y=[]
B=[]
s=float(0)
for i in range(n):
    Y.append(round((math.pow(i,2)-2*i-19.3*math.cos(i)),3))
    s=s+Y[i]
s=round(s/n,3)
print('Массив Y: ',Y)
for i in range(n):
    if Y[i]<s:
        B.append(Y[i])
for i in range(n):
    if Y[i]==s:
        B.append(Y[i])
for i in range(n):
    if Y[i]>s:
        B.append(Y[i])
print('Новый массив: ',B)






