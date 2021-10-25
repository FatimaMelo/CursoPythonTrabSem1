print('Conversão de temperatura em Celsius para Kelvin')
print('Iniciar Conversão? use s para "sim" e n para "não"')
resp = input()

while resp == 's':
    print('Digite a temperatura Celsius: ')
    c = float(input())
    k = c + 273.15
    print(f'A temperatura em graus Celsius é {c} e em graus Kelvin é: {k:.2f}')

    print('Continuar? use s para "sim" e n para "não"')
    resp = input()

print('Obrigada por utilizar o sistema!')