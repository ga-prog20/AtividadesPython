n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))

media =(n1 + n2) / 2

if media >= 6:
    print('Você foi aprovado!')
elif media >= 5 and media < 6:
    print('Você ficou de exame!')
else:
    print('Você foi reprovado!')
    