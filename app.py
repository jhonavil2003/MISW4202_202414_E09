from datetime import datetime
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from modelos import db
from vistas.vistas import VistaCliente, VistaPlan, VistaSolicitud

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///abcall.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

api = Api(app)
jwt = JWTManager(app)

db.init_app(app)
db.create_all()

cors = CORS(app)



api.add_resource(VistaCliente, '/clientes')
api.add_resource(VistaSolicitud, '/solicitudes')
api.add_resource(VistaPlan, '/planes')
