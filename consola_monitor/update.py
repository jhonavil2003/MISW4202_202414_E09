from sqlalchemy.orm import Session
from config import SessionLocal
from models import Solicitud

def update_solicitud_status(solicitud_id: int, new_status: str):
    db = SessionLocal()
    try:
        solicitud = db.query(Solicitud).filter(Solicitud.id == solicitud_id).first()
        if solicitud:
            solicitud.descripcion = new_status
            db.commit()
            print(f"Solicitud {solicitud.id} actualizada a estado {new_status}")
        else:
            print(f"Solicitud con ID {solicitud_id} no encontrada.")
    except Exception as e:
        db.rollback()
        print(f"Error al actualizar la solicitud: {e}")
    finally:
        db.close()