from pydantic import ModelBase

class Medico(ModelBase):
    nombre_med: str
    cedula: int
    especialidad: str
    universidad: str
    dom_consultorio: str
