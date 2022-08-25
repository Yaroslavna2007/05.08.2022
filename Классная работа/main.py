x = str(input('введите строку '))
a = 'abcdefghijklmnopqrstuvwxyz'
for y in range(len(x)):
        s = a.find(x[y])
        s = s+5
        d = s
print(a[0:d])