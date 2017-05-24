import random
import array
n=int(input('Размерность: '))
A=[]
B=[]
mi=10
for i in range(n):
    A.append([])
    for j in range(n):
        A[i].append(random.randint(0, 9))
print('Исходная матрица')
for i in A:
    print(i)
for i in range(n):
    if A[i][i]<=mi:
        mi=A[i][i]
ib=0
for i in range(n):
    if A[i][i]!=mi:
        B.append([])
        for k in range(n):
            B[ib].append(A[i][k])
        ib=ib+1
print('Матрица B')
for i in B:
    print(i)

            
        




        
        
        

