s1=input('Введите первое слово: ')
s2=input('Введите второе слово: ')
f=int(0)
for i in range(0,len(s1)):
    for j in range(0,len(s2)):
        if s2[j]==s1[i]:
            f=1  
    if f==1 and s1[i]!=' ':
        print(s1[i],' Да ')
    elif s1[i]!=' ':
        print(s1[i],' Нет ')
    s1=s1.replace(s1[i],' ')
    f=0
            
        
