n=int(input('Введите N - '))
t=int(0)
while n>=5 :
    if n%5 ==0 :
        t=1
        print(n)
    n=n-1
if t ==0:
    print('Нет чисел кратных 5')

