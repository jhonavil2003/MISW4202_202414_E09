from celery import Celery

# Configurar Celery
app = Celery('consolas', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')


# Configuración adicional de Celery (opcional)
app.conf.update(
    result_expires=3600,
)

if __name__ == '__main__':
    app.start()