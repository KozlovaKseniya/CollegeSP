import math
k=int(input('Введите k - '))
w=float(0)
if k == 4:
    for i in range(-2,4):
        w=w+(math.pow(-1,i)*math.factorial(i+3))/(i-4)   
elif k<4:
    for i in range(-2,k+1):
        w=w+(math.pow(-1,i)*math.factorial(i+3))/(i-4)
elif k>4:  
    for i in range(-2,4):
        w=w+(math.pow(-1,i)*math.factorial(i+3))/(i-4)
    for i in range(5,k+1):
        w=w+(math.pow(-1,i)*math.factorial(i+3))/(i-4)   
print('W = ',w)
