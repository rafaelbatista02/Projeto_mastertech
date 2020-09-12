from flask_marshmallow import Marshmallow
from .model import Cadastro 

ma = Marshmallow()


def configure(app):
    ma.init_app(app)

    
class CadasSchema(ma.ModelShema):
    class meta:
        model = Cadastro
