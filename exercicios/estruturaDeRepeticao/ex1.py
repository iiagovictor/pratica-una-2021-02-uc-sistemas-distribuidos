nota = int(input('Informe a nota: '))

while (nota < 0) or (nota > 10):
    print('Valor da nota inválido')
    nota = int(input('Informe a nota: '))