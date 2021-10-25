print('Conversão de temperatura em Celsius para Fahrenheit')
print('Iniciar Conversão? use s para "sim" e n para "não"')
resp = input()

while resp == 's':
    print('Digite a temperatura Celsius: ')
    c = float(input())
    print(c)

    f = c * (9/5)+32
    print(f'A temperatura em graus Celsius é: {c} e em graus Fahrenheit é: {f}')

    print('Continuar? use s para "sim" e n para "não"')
    resp = input()

print('Obrigada por utilizar o sistema!')