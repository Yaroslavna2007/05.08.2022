x = str(input('введите строку'))
s = x.find('h')
a = x.rfind('h')
q = x[0:s]
l = x[a+1:]
print(q + l)