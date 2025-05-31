from pydantic import ModelBase
from time import datetime

class Expediente(ModelBase):
    fecha: datetime
    medico: str
    diagnostico: str

