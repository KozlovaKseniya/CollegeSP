import array
n=int(20)
a = []
c1=0
c2=0
for i in range(0,n):
    a.append(int(input('a=')))
for x in a:
    if x%2==0:
        c1=c1+1
    else:
        c2=c2+1
print(a)
print('Нечетные: ',c1)
print('Четные: ',c2)
if c1==c2:
    print('Количество четных=количество нечетных')
elif c1>c2:
    print('Нечетных чисел больше')
if c1<c2:
    print('Четных чисел больше')
    
    



    
