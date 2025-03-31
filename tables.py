from peewee import Model, IntegerField, TextField, CharField, ForeignKeyField, FloatField, DateTimeField
from database import db

class BaseModel(Model):
    class Meta:
        database = db

class DatosPaciente(BaseModel):
    id = IntegerField(primary_key=True)
    nombre = CharField(max_length=50)
    apellido_paterno = CharField(max_length=50)
    apellido_materno = CharField(max_length=50)
    edad = IntegerField()
    peso = FloatField()
    altura = FloatField()
    fecha_nacimiento = DateTimeField()

class Medico(BaseModel):
    nombre_med = CharField(max_length=110)
    cedula = IntegerField()
    especialidad = CharField(max_length=70)
    universidad = CharField(max_length=80)
    dom_consultorio = CharField(max_length=150)

class SignosPaciente(BaseModel):
    fecha_visita = DateTimeField()
    temperatura = FloatField()
    fr = CharField(max_length=10)
    fc = CharField(max_length=10)
    t_a = CharField(max_length=10)
    spo2 = FloatField()
    diagnostico = TextField()
    tx = TextField()

class Expediente(BaseModel):
    fecha = DateTimeField()
    medico = CharField(max_length=110)
    diagnostico = TextField()


def migrate_tables():
    try:
        with db as conn:
            conn.connect()
            conn.create_tables()
    except Exception as e:
        print(f"Ha ocurrido un error al crear las tablas: /n {e}")
    
