from flask import Blueprint, current_app, request, jsonify
from .model import Cadastro
from .serealizer import CadasSchema
import datetime

hora = datetime.now()


bp_cadastro = Blueprint('cadastro',__name__)

@bp_cadastro.route('/mostrar', methods=['GET'])
def mostrar():
    bs = CadasSchema(many=True)
    result = Cadastro.query.all()
    
    return bs.jsonify(result, hora), 200
    

@bp_cadastro.route('/cadastrar', methods=['GET'])
def cadastrar():
    bs = CadasSchema()
    cadastro, error = bs.load(request.json)
    current_app.db.session.add(cadastro)
    current_app.db.session.commit()

    return bs.jsonify(cadastro, hora)



@bp_cadastro.route('/alterar/<identificador>', methods=['POST'])
def alterar(identificador):
    bs = CadasSchema()
    query = Cadastro.query.filter(Cadastro.id == identificador)
    query.update(request.json)
    current_app.db.session.commit()
    
    return bs.jsonify(query.first(), hora)


@bp_cadastro.route('/deletar/<identificador>', methods=['GET'])
def deletar(identificador):
    Cadastro.query.filter(Cadastro.id == identificador). delete()
    current_app.db.session.commit()
    
    return jsonify("Deletado com sucesso", hora)


        