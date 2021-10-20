import requests

url = 'https://viacep.com.br/ws/'
cep = '30140071'
formato = '/xml/'

resposta = requests.get(url + cep + formato)

if (resposta.status_code == 200):
 print()
 print('XML: ', resposta.text)
 print()
else:
 print('XMS: ', resposta.text)
