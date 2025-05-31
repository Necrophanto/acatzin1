from pydantic import ModelBase
from time import datetime

class SignosPaciente(ModelBase):
    fecha_visita: datetime
    temperatura: float
    fr: str
    fc: str
    t_a: str
    spo2: float
    diagnostico: str
    tx: str
