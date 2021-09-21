altura = float(input('Informe sua altura em METROS: '))
genero = input('Informe seu gênero, H para HOMEM e M para MULHER: ')

if genero == 'H':
    peso_Ideal = (72.7 * altura) - 58
    print('Seu peso ideal é : ',round(peso_Ideal),' KG')
else:
    peso_Ideal = (62.1 * altura) - 44.7
    print('Seu peso ideal é : ',round(peso_Ideal),' KG')
