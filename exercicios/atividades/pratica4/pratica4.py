import sqlite3
from sqlite3 import Error
from flask import Flask, request, jsonify
from datetime import date

app = Flask(__name__)

# Método GET

@app.route('/produto/pesquisar/<int:id_produto>', methods=['GET'])

def pesquisar(id_produto=None):
    if id_produto == None:
        return jsonify({'mensagem': 'parametro invalido'})
    else:
        try:
            mydb = sqlite3.connect('exercicios/atividades/pratica4/db-produtos-v2.db')

            if id_produto == 0:
                sql = "SELECT * FROM produtos"
            else:
                sql = 'SELECT * FROM produtos WHERE id_produto = ' + str(id_produto)

            cur = mydb.cursor()
            cur.execute(sql)
            registros = cur.fetchall()

            if registros:
                nomes_colunas = [x[0] for x in cur.description]

                json_dados = []
                for reg in registros:
                    json_dados.append(dict(zip(nomes_colunas, reg)))

                return jsonify(json_dados)
            else:
                return jsonify({'mensagem': 'registro nao encontrado'})

        except Error as msg_error:
            return jsonify({'mensagem': msg_error})
        finally:
            mydb.close()

# Método DELETE

@app.route('/produto/excluir/<int:id_produto>', methods=['DELETE'])

def excluir(id_produto=None):

    if id_produto == None:
        return jsonify({'mensagem': 'parametro invalido'})
    else:
        try:
            mydb = sqlite3.connect('exercicios/atividades/pratica4/db-produtos-v2.db')

            sql = 'DELETE FROM produtos WHERE id_produto = ' + str(id_produto)

            cur = mydb.cursor()
            cur.execute(sql)

            mydb.commit()

            return jsonify({'mensagem': 'registro excluido'})

        except Error as msg_error:
            return jsonify({'mensagem': msg_error})
        finally:
            mydb.close()

# Método POST

@app.route('/produto/inserir', methods=['POST'])

def inserir():

    if request.method == 'POST':
        dados = request.get_json()
        data_criacao = date.today()
        descricao = dados['descricao']
        preco = dados['preco']
        qtd = dados['qtd']

        if data_criacao and descricao and preco and qtd:
            registro = (descricao, preco, qtd, data_criacao)

            try:
                mydb = sqlite3.connect('exercicios/atividades/pratica4/db-produtos-v2.db')

                sql = 'INSERT INTO produtos(descricao, preco, qtd, data_criacao) VALUES(?,?,?,?)'
                cur = mydb.cursor()
                cur.execute(sql, registro)
                mydb.commit()

                return jsonify({'mensagem': 'registro inserido com sucesso'})

            except Error as msg_error:
                return jsonify({'mensagem': msg_error})
            finally:
                mydb.close()

    else:
        return jsonify({'mensagem': 'campos <descricao> msg_error <preco> sao obrigatorios'})

# Método PUT

@app.route('/produto/alterar', methods=['PUT'])

def alterar():

    if request.method == 'PUT':

        dados = request.get_json()
        data_atualizacao = date.today()
        descricao = dados['descricao']
        preco = dados['preco']
        id_produto = dados['id_produto']

        if data_atualizacao and descricao and preco and id_produto:
            registro = (descricao, preco, data_atualizacao, id_produto)

            try:
                mydb = sqlite3.connect('exercicios/atividades/pratica4/db-produtos-v2.db')

                sql = 'UPDATE produtos SET descricao=?, preco=?, data_atualizacao=? WHERE id_produto=?'
                cur = mydb.cursor()
                cur.execute(sql, registro)
                mydb.commit()

                return jsonify({'mensagem': 'registro alterado com sucesso'})

            except Error as msg_error:
                return jsonify({'mensagem': msg_error})
            finally:
                mydb.close()

    else:
        return jsonify({'mensagem': 'campos <descricao>, <preco> msg_error <id_produto> sao obrigatorios'})


# Método de rota não localizada

@app.errorhandler(404)
def endpoint_nao_encontrado(msg_error):
    return jsonify({'mensagem': 'erro - endpoint nao encontrado'}), 404


# Execucao

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")