import random
import array
m=int(input('Количество строк: '))
n=int(input('Количество столбцов: '))
A=[]
k=0
for i in range(n):
    A.append([])
    for j in range(n):
        A[i].append(random.randint(0, 100))
for i in A:
    print(i)
for i in range (1,n):
    if set(A[i])in set(A[0]):
        k=k+1
print('Количество строк, похожих на первую: ',k)


        
