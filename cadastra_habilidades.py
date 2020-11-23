import json
from flask import request
from flask_restful import Resource
from habilidades import lista_habilidades


class CadastraHabilidades(Resource):
    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self, id):
        lista_habilidades.pop(id)
        return {"status": "sucesso", "mensagem": "Registro excluído!"}

