print('Conversão de temperatura em Kelvin para Celsius')
print('Iniciar Conversão? use s para "sim" e n para "não"')
resp = input()

while resp == 's':
    print('Digite a temperatura Kelvin: ')
    k = float(input())
    c = k - 273.15
    print(f'A temperatura em graus Kelvin é {k} e em graus Celsius é: {c:.2f}')

    print('Continuar? use s para "sim" e n para "não"')
    resp = input()

print('Obrigada por utilizar o sistema!')