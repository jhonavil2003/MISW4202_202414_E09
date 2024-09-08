from celery_config import app

def submit_task():
    # Enviar la tarea al worker de Celery sin parámetros
    result = app.send_task('tasks.process_solicitud')
    print(f"Tarea enviada con ID: {result.id}")

if __name__ == "__main__":
    submit_task()