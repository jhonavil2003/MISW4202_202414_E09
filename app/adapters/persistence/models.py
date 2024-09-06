from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from enums.enums import Estado, TipoPlan
from ...extensions import db


class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), nullable=False)
    solicitudes = db.relationship('Solicitud', backref='cliente', lazy=True)

class Solicitud(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.Enum(Estado), nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)
    fecha_inicio = db.Column(db.DateTime, nullable=False)
    fecha_fin = db.Column(db.DateTime, nullable=True)
    codigo = db.Column(db.String(50), nullable=False, unique=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_plan = db.Column(db.Enum(TipoPlan), nullable=False)
    clientes = db.relationship('Cliente', backref='plan', lazy=True)    
