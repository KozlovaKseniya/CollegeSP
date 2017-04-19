x=float(input('Введите 6-значное число - '))
t2=int(0)
t1=int(0)
if 0<x//100000<9:
    while x>999:
        t2=t2+(x%10)
        x=x//10
    while x!=0:
        t1=t1+(x%10)
        x=x//10
    if t2==t1:
        print('Счастливый билет')
    else:
        print('Не Счастливый билет')
else:
    print('Число не 6-значное')
    
        
        
        
