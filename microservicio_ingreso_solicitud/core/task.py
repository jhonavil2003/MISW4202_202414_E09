from ..extensions import db 
from ..adapters.persistence.models import Solicitud
from datetime import datetime
from ..celery_config import celery
import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=1)

@celery.task(bind=True)
def process_solicitud(self, *args, **kwargs):
    redis_key = f'task-args-{self.request.id}'
    redis_data = json.dumps({'args': args[0], 'kwargs': kwargs})
    redis_client.set(redis_key, redis_data)
    return f"solicitud-generada: {args[0]}"