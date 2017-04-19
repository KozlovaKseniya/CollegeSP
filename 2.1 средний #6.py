v = float(input("Вклад="))
s= float
if v < 5000:
    print("процент годовых 20%")
    s=v+v*0.2
    print('Сумма выплаты',s)
elif  5000<=v<10000:
    print("процент годовых 22%")
    s=v+v*0.22
    print('Сумма выплаты',s)
