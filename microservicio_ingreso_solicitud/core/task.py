from ..extensions import db 
from ..adapters.persistence.models import Solicitud
from datetime import datetime
from ..celery_config import celery


@celery.task
def process_solicitud(solicitud_id):
    with celery.app.app_context():
            solicitud = Solicitud.query.get(solicitud_id)
            if solicitud:
                solicitud.fecha_procesamiento = datetime.utcnow()
                db.session.commit()
                return f"Solicitud {solicitud_id} procesada."