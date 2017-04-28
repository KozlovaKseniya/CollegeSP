s=input('Введите строку: ')
s2=''
for i in range(0,len(s)):
    if s[i]=='я':
        s2=s2+' '
    else:
        s2=s2+chr(ord(s[i])+1)
s=s2     
print(s)
