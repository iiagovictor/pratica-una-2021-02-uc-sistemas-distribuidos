import sqlite3
import requests
from datetime import date

# Database connection

mydb = sqlite3.connect('c:/Users/iagov/Downloads/pratica-una-2021-02-uc-sistemas-distribuidos/exercicios/atividadePratica/pratica2/bdcotacoes.db')
cursor = mydb.cursor()

# API Key Variables

api = 'https://api.hgbrasil.com/finance?format=json-cors&key='
chave = '558afd34'

# Searching and returningJSON through via API key

retorno = requests.get(api + chave)
json = retorno.json()
    
if (retorno.status_code == 200):
    print('JSON retornado com sucesso')
else:
    print('Nenhum retorno')

# Insertion script in DB.

sql = "INSERT INTO moedas (data, real, dolar, euro) VALUES (?,?,?,?)"

# Value got from buy > USD and EUR in JSON, and formated date.

current_date = date.today()
formatted_date = current_date.strftime('%d/%m/%Y')
print(current_date)
print(formatted_date)

buyUSD = json['results']['currencies']['USD']['buy']
print(buyUSD)

buyEUR = json['results']['currencies']['EUR']['buy']
print(buyEUR)

real = 1.000
print(real)

values = (formatted_date, real, buyUSD, buyEUR)
print(values)

# Set in DB

cursor.execute(sql, values)

# Closed conection with DB.

mydb.commit()
mydb.close()