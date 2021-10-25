
print('Conversão de velocidade em km/h para m/s')
print('Iniciar Conversão? use s para "sim" e n para "não"')
resp = input()

while resp == 's':
    print('Digite a velocidade em km/h: ')
    km = float(input())
    ms = km/3.6
    print(f'A velocidade {km} em km/h é igual à velocidade {ms:.2f} em m/s')

    print('Continuar? use s para "sim" e n para "não"')
    resp = input()

print('Obrigada por utilizar o sistema!')