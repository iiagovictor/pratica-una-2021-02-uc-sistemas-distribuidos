pais_a = int(input('Informe a a população do país A: '))
taxaCrescimentoA = float(input('Informe a taxa de crescimento ANUAL do país A: '))
pais_b = int(input('Informe a a população do país B: '))
taxaCrescimentoB = float(input('Informe a taxa de crescimento ANUAL do país B: '))

anos = 0

print('Populacao País A: ', pais_a)
print('Populacao País B: ', pais_b)

while pais_a <= pais_b:
    pais_a = pais_a + (pais_a * (taxaCrescimentoA/100))
    pais_b = pais_b + (pais_b * (taxaCrescimentoB/100))
    anos = anos + 1

print('Número de anos para o País A igualar ou ultrapassar a populacao do País B: ', anos)