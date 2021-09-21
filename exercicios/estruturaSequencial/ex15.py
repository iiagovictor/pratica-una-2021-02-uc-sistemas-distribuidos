valor_hora = float(input('Quanto você ganha por hora: R$ '))
horas_trabalhada = float(input('Quantas horas você trabalhou neste mês: '))

salario_bruto = valor_hora * horas_trabalhada

imposto_renda = (salario_bruto * 0.11)
inss = (salario_bruto * 0.08)
sindicato = (salario_bruto * 0.05)
salario_liquido = salario_bruto - imposto_renda - inss - sindicato


print('Salário bruto: R$',round(salario_bruto,2))
print('IR (11%): R$',round(imposto_renda,2))
print('INSS(8%): R$',round(inss,2))
print('Sindicato: R$',round(sindicato,2))
print('O salário líquido é: R$', round(salario_liquido,2))
