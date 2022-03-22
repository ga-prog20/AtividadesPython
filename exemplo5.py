idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Você pode ter uma CNH!')
elif idade >= 16 and idade < 18:
    print('Falta pouco tempo para tirar!')
else:
    print('Você ainda não está apto para ter uma CNH!')
