nome = input('Digite o nome de usuário: ')
senha = input('Digite a senha: ')

while nome == senha:
    print('Nome de usuario e senha não podem ser iguais, tente novamente!')
    nome = input('Digite o nome de usuário: ')
    senha = input('Digite a senha: ')

print('Conta criada com sucesso!')