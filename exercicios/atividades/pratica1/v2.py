import requests

url = 'https://viacep.com.br/ws/'
ceps = ['30140071', '30140072', '30140073', '30140074', '30140075']
formato = '/json/'

    
for cep in ceps:

    resposta = requests.get(url + cep + formato)

    if (resposta.status_code == 200):
        print()
        print('JSON: ', resposta.json())
        print()
    else:
        print('JSON: ', resposta.json())
