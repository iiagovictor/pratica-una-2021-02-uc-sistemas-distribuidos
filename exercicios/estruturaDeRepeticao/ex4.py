pais_a = 80000
pais_b = 200000

anos = 0

print('Populacao País A: ', pais_a)
print('Populacao País B: ', pais_b)

while pais_a <= pais_b:
    pais_a = pais_a + (pais_a * 0.03)
    pais_b = pais_b + (pais_b * 0.015)
    anos = anos + 1

print('Número de anos para o País A igualar ou ultrapassar a populacao do País B: ', anos)