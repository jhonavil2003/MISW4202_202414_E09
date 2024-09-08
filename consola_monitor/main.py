# import sys
# from update import update_solicitud_status

# def main():
#     if len(sys.argv) != 3:
#         print("Uso: python main.py <solicitud_id> <nuevo_estado>")
#         return

#     solicitud_id = int(sys.argv[1])
#     nuevo_estado = sys.argv[2]

#     update_solicitud_status(1, "pepe")

# if __name__ == "__main__":
#     main()

import time
from celery.result import AsyncResult
from sqlalchemy.orm import Session
from config import SessionLocal
from models import Solicitud
from celery_config import celery

def update_solicitud_status(db: Session, task_id: str, status: str):
    solicitud = db.query(Solicitud).filter(Solicitud.task_id == task_id).first()
    if solicitud:
        solicitud.estado = status
        db.commit()
        print(f"Solicitud {solicitud.id} actualizada a estado {status}")

def monitor_tasks():
    db = SessionLocal()
    while True:
        # Obtén todas las tareas activas y reservadas
        i = celery.control.inspect()
        active_tasks = i.active()
        reserved_tasks = i.reserved()
    
        tasks = []
        if active_tasks:
            for worker, tasks_list in active_tasks.items():
                tasks.extend(tasks_list)
        
        if reserved_tasks:
            for worker, tasks_list in reserved_tasks.items():
                tasks.extend(tasks_list)
        
        for task in tasks:
            task_name = task['name']
            if task_name == 'microservicio_ingreso_solicitud.core.task.process_solicitud':
                task_id = task['id']
                task_status = task['state']
                if task_status == 'RECEIVED':
                    update_solicitud_status(db, task_id, task_status)
        
        # Espera un tiempo antes de la siguiente iteración
        time.sleep(5)

if __name__ == "__main__":
    monitor_tasks()