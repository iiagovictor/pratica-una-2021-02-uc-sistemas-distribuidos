nome = str(input('Informe seu nome: '))

if (len(nome) <= 3):
    nome = str(input('Informe um nome válido: '))

idade = int(input('Informe sua idade: '))

if (idade < 0) or (idade > 150):
     idade = int(input('Informe uma idade válida: '))

salario = float(input('Informe seu salário: R$ '))

if (salario <= 0):
     salario = float(input('Seu salário deve ser maior que R$ 0,00. Digite novamente: R$ '))

sexo = str(input('Informe seu sexo, sendo (F) para feminino e (M) para masculino: '))

if (sexo != 'M') or (sexo != 'F'):
    sexo = str(input('Informe seu sexo, sendo (F) para feminino e (M) para masculino: '))

estadoCivil = str(input('Informe seu estado civil, sendo (S) para solteiro, (C) para casado, (V) para viúvo e (D) para divorciado: '))

if (estadoCivil != 'S') or (estadoCivil != 'C') or (estadoCivil != 'V') or (estadoCivil != 'D'):
    estadoCivil = str(input('Informe seu estado civil, sendo (S) para solteiro, (C) para casado, (V) para viúvo e (D) para divorciado: '))