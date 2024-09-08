from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ...extensions import db

class Integracion(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    mensaje = db.Column(db.JSON, nullable=False)
    codigo_solicitud = db.Column(db.String, nullable=False)