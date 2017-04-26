import random
n=int(input('Введите N - '))
m=float(input('Введите M>0 - '))
k = [random.randrange(0, m) for i in range(n)]
nmin=int(m)
t=int(0)
print(k)
for i in range(n):
    if 3*k[i]>m and k[i]<nmin:
        nmin=k[i]
        t=1
if t ==1:     
    print('Наименьшее целое',nmin)
    print('3k = ',3*nmin)
else:
    print('Нет такого числа')



 

