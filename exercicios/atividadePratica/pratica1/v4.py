import requests

url = 'https://viacep.com.br/abc/'
cep = '30140071'
formato = '/json/'

resposta = requests.get(url + cep + formato)

if (resposta.status_code == 200):
    print()
    print('JSON : ', resposta.json())
    print()
else:
    print('Nao houve sucesso na requisicao.')
    print('Erro: ', resposta.status_code)
    print(resposta.text)