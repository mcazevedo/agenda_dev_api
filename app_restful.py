from flask import Flask, request
from flask_restful import Resource, Api
import json
from habilidades import Habilidades
from cadastra_habilidades import CadastraHabilidades

app = Flask(__name__)
api = Api(app)

desenvolvedores = [

    {"id": "0",
     "nome": "Matheus",
     "habilidades": ["Python", "Flask"]},
    {"id": "1",
     "nome": "Azevedo",
     "habilidades": ["Python", "Django"]}
]

# Devolve, atualiza ou deleta um desenvolvedor por ID
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            response = {"status": "Erro", "mensagem": f"desenvolvedor de ID {id} não existe"}
        except Exception:
            response = {"status": "Erro", "mensagem": "mensagem de erro desconhecido, procure o ADM"}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {"status": "sucesso", "mensagem": "Registro excluído!"}

# Lista todos os desenvolvedores e inclui um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>')
api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(CadastraHabilidades, '/habilidades/<int:id>')


if __name__ == '__main__':
    app.run(debug=True)
