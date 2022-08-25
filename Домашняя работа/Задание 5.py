x = str(input('введите строку'))
s = x.find('h')
a = x.rfind('h')
print(x[:s]+x[a:s:-1]+x[a:])