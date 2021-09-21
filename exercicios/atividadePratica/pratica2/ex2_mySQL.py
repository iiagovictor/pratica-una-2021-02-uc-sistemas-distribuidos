import mysql.connector
import requests
from datetime import date

# Conexão com banco de dados

mydb = mysql.connector.connect(
    host='localhost',
    user='root', 
    password='Vh-Nkjv-g66-QZGvBc.qD-6KqEyHx..4U@MKhRVhf-vBdgEvH*',
    database='bdcotacoes')
cursor = mydb.cursor()

# Váriaveis da chave API

api = 'https://api.hgbrasil.com/finance?format=json-cors&key='
chave = '558afd34'

# Buscando e retornando o JSON através da chave API

retorno = requests.get(api + chave)
json = retorno.json()
    
if (retorno.status_code == 200):
    print('JSON retornado com sucesso')
else:
    print('Nenhum retorno')

# Script de inserção no DB.

sql = "INSERT INTO moedas (data, dolar, euro) VALUES (%s, %s, %s)"

# Pegando o valor de compra do USD e EUR no JSON.

current_date = date.today()
formatted_date = current_date.strftime('%d/%m/%Y')
print(current_date)
print(formatted_date)

buyUSD = json['results']['currencies']['USD']['buy']
print(buyUSD)
buyEUR = json['results']['currencies']['EUR']['buy']
print(buyEUR)

values = (formatted_date, buyUSD, buyEUR)
print(values)

cursor.execute(sql, values)

# Fechando conexão do DB.

mydb.close()