import redis
import json
import re
from marshmallow import ValidationError
from sqlalchemy.orm import sessionmaker
from microservicio_proceso_solicitud.core.schemas import IntegracionSchema
from microservicio_proceso_solicitud.adapters.persistence.models import Integracion
from microservicio_proceso_solicitud.extensions import db 
from flask import Flask, jsonify


class IntegracionService:
    @staticmethod
    def get_all_solicitudes_queue():

        integracion_schema=IntegracionSchema()
        r = redis.Redis(host='localhost', port=6379, db=1)
        integracion_schema = IntegracionSchema()  

        keys = r.keys('celery-task-meta-*')

        try:
            for key in keys:
                result_data = r.get(key)

                if result_data:
                    result_data = result_data.decode('utf-8')
                    result_json = json.loads(result_data)

                    if result_json.get('status') == 'SUCCESS':
                        result = result_json.get('result', '')

                        match = re.search(r':\s*(.*)', result)
                        if match:
                            result_after_colon = match.group(1).strip()
                             # Reemplazar comillas simples con comillas dobles
                            result_after_colon = result_after_colon.replace("'", '"')
                            result_after_colon = result_after_colon.replace('None', 'null')

                            try:
                                data_from_json = json.loads(result_after_colon)
                                estado = data_from_json['estado']
                                print(f"Estado: {estado}")

                            except json.JSONDecodeError as e:
                                print('Error al decodificar JSON:', str(e))
                            except KeyError as e:
                                print('Clave no encontrada en el JSON:', str(e))
                            except Exception as e:
                                print('No se puede convertir a JSON:', str(e))

        except Exception as e:
            print('Error al guardar datos en la base de datos:', str(e))

