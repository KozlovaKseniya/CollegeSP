import array
import math
ch=str(input('Введите число в двоичной системе счисления:'))
t1=int(0)
t2=int(0)
arr1=[]
arr2=[]
arr3=[]
for i in range(len(ch)):
    arr1.append(ch[i]) 
for i in arr1:
    if i!='.':
        arr2.append(i)
        t1=t1+1
    else:
        break
for i in reversed(arr1):
    if i!='.':
        arr3.append(i)
        t2=t2+1
    else:
        break










    

 
 
