import enum

class Estado(enum.Enum):
    ACTIVO = 'activo'
    CERRADO = 'cerrado'
    BLOQUEADO = 'bloqueado'
    POR_ASIGNAR = 'por_asignar'

class TipoPlan(enum.Enum):
    EMPRENDEDOR = 'emprendedor'
    EMPRESARIO = 'empresario'
    EMPRESARIO_PLUS = 'empresario_plus'