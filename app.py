import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from extensions import db, cors
from adapters.api.routes import register_routes
from flask_restful import Api

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', f'sqlite:///{os.path.join(os.path.abspath(os.path.dirname(__file__)), "abcall.db")}')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

db.init_app(app)
cors.init_app(app)

with app.app_context():
    db.create_all()
    
api = Api(app)
register_routes(api)

app.config['DEBUG'] = os.environ.get('FLASK_DEBUG')

if __name__ == '__main__':
    app.run()