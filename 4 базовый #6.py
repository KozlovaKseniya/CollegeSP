s=input('Введите строку: ')
t=int(0)
c='0123456789'
for i in range(len(s)):
        for j in range(len(c)):
            if s[i]==c[j]:
                t=t+1
print('Количество символов цифр - ',t)
    
