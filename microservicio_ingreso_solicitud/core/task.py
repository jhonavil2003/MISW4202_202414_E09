from ..extensions import db 
from ..adapters.persistence.models import Solicitud
from datetime import datetime
from ..celery_config import celery


@celery.task
def process_solicitud(solicitud_id):
    data = "datos estáticos"
    # Aquí va la lógica para procesar la solicitud
    print(f"Procesando solicitud con datos: {data}")
    return f"Solicitud procesada con datos: {data}"