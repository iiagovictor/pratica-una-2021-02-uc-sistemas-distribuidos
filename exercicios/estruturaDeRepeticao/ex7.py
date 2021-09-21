memoria = 0

for i in range(5):
    numero = int(input('Informe um númemro: '))
    if numero > memoria:
        memoria = numero

print('O maior número informado é: ', memoria)

