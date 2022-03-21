import math

a = float(input('Digite o ângulo em graus:'))

s = float(input('Digite a extensão da sombra em metros'))

a = math.radians(a)

h = s * math.tan(a)

print(f'A altura do prédio é {h:.2f} metros')
