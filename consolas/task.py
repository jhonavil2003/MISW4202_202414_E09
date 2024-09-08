from .celery_config import app

@app.task
def process_solicitud():
    # Datos estáticos para la solicitud
    data = "datos estáticos"
    # Aquí va la lógica para procesar la solicitud
    print(f"Procesando solicitud con datos: {data}")
    return f"Solicitud procesada con datos: {data}"