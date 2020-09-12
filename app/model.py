from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

class Cadastro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_compelto = db.Column(db.String(150))
    

    
    



