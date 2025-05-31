from pydantic import ModelBase
from time import datetime

class DatosPaciente(ModelBase):
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    edad: int
    peso: float
    altura: float
    fecha_nacimiento: datetime

class Medico(ModelBase):
    nombre_med: str
    cedula: int
    especialidad: str
    universidad: str
    dom_consultorio: str

class SignosPaciente(ModelBase):
    fecha_visita: datetime
    temperatura: float
    fr: str
    fc: str
    t_a: str
    spo2: float
    diagnostico: str
    tx: str

class Expediente(ModelBase):
    fecha: datetime
    medico: str
    diagnostico: str
