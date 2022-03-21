a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

if a > b and b < c:
    print('O menor valor é o b')
elif c < b and b > c:
    print('O menor valor é o c')
else:
    print('O menor valor é o a')