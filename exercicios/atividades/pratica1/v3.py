from typing import Text
import requests

url = 'https://viacep.com.br/ws/'
uf = 'MG/'
localidade = 'Belo%20Horizonte'
logradouro = 'Rua%20Dos%20Aimorés'
formato = '/json/'

resposta = requests.get(url + uf + localidade + logradouro + formato)
    
if (resposta.status_code == 200):
    print()
    lista = resposta.json()
    print('JSON: ', lista)
    print()
    print('Apenas o primeiro item: ', lista[0])
else:
    print(resposta.json())