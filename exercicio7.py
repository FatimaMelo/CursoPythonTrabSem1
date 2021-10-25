print('Conversão de temperatura em Fahrenheit para Celsius')
print('Iniciar Conversão? use s para "sim" e n para "não"')
resp = input()

while resp == 's':
    print('Digite a temperatura Fahrenheit: ')
    f = float(input())
    c = 5 * (f - 32) / 9
    print(f'A temperatura em graus Fahrnheit é: {f} e em graus Celsius é: {c}')

    print('Continuar? use s para "sim" e n para "não"')
    resp = input()

print('Obrigada por utilizar o sistema!')