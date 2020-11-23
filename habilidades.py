import json
from flask import request
from flask_restful import Resource

lista_habilidades = ["Python", "Java", "PHP"]


class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        lista_habilidades.append(dados)
        response = lista_habilidades[posicao]
        return response

