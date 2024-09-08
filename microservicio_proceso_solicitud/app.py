from microservicio_proceso_solicitud import create_app
from flask_restful import Api
from microservicio_proceso_solicitud.adapter.api.routes import register_routes
from microservicio_proceso_solicitud.extensions import db, cors

app = create_app('default')
app_context = app.app_context()
app_context.push()

with app.app_context():
    cors.init_app(app)
    api = Api(app)
    register_routes(api)

