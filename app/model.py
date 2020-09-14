from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Cadastro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_compelto = db.Column(db.String(150))
    cpf = db.Column(db.Integer)
    email = db.Column(db.String, unique=True)
    data_de_nascimento = db.Column(db.Integer)

def __init__(self, nome_compelto, cpf, email, data_de_nascimento):
    self.nome_compelto = nome_compelto
    self.cpf = cpf
    self.email = email
    self.data_de_nascimento = data_de_nascimento

def __repr__(self):
    return "<User %r>" % self.id


    

    
    



