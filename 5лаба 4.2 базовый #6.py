import random
import array
m1=0
m3=0
A=[]
for i in range(4):
    A.append([])
    for j in range(3):
        A[i].append(random.randint(0, 9))
print('Исходная матрица')
for i in A:
    print(i)
for i in range(4):
    if A[i][0]>m1:
        m1=A[i][0]
for i in range(4):
    if A[i][2]>m3:
        m3=A[i][2]
for i in range(4):
    if A[i][2]==m3:
        A[i][2]=m1 
for i in range(4):
    if A[i][0]==m1:
        A[i][0]=m3 
print('Результат:')
for i in A:
    print(i)

