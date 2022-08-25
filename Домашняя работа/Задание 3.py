x = str(input('введите строку'))
s = x.find('f',2)
d = x. count('f')
if d== 0:
    print(-2)
elif d==1:
    print(-1)
else:
    print(s)