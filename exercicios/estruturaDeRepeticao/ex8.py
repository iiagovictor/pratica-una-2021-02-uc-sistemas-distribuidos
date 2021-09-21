contador = 0
somador = 0

for i in range(5):
    numero = int(input('Informe um númemro: '))
    somador = somador + numero
    contador = contador + 1

print('A soma dos números informados é: ', somador)
print('A média dos números informados é: ', somador/contador)