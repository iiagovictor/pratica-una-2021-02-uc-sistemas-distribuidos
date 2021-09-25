from flask import Flask
import requests

app = Flask(__name__)

@app.route('/consultacep/<cep>', methods=['GET'])
def home(cep):
    url = 'https://viacep.com.br/ws/'
    formato = '/json/'

    resposta = requests.get(url + cep + formato)

    if (resposta.status_code == 200):
        return (resposta.json())
    else:
        return (resposta.json())

app.run(host='0.0.0.0', port=80)