import requests

resposta = requests.get('http://www.google.com/search', params={'q': 'Iago Victor'})

if (resposta.status_code == 200):
    print('Retorno : ', resposta.text)
    arquivo = open('c:\\temp\\d_google.html', 'w')
    arquivo.write(resposta.text)
    arquivo.close()
else:
    print('Nao houve sucesso na requisicao.')