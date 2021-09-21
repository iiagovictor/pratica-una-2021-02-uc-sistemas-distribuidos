quant_peixe = float(input('Informe a quantidade em KG de peixes: '))

if (quant_peixe > 50):
    print('Peso de peixes ultrapassou o estebelecido pelo regulamento.')
    excesso = quant_peixe - 50
    print('Excesso: ',excesso)
    multa = (quant_peixe - 50) * 4
    print('Multa a pagar pelo excesso: R$ ',round(multa,2))
else:
    print('Peso de peixes dentro do estebelecido pelo regulamento.')