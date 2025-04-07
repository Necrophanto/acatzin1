import sqlite3
from pydantic import BaseModel, Field, get_type_hints
from pypika import Table, create_table, Column
from pypika.enums import SqlTypes
import inspect

class ModelBase(BaseModel):
    pass

class Paciente(ModelBase):
    nombre: str
    apellido_paterno: str
    apellido_materno: str
    edad: int
    peso: float
    altura: float

def create_table_pypika(model_class, db_connection):
    """Creates an SQLite table from a Pydantic BaseModel using PyPika."""

    table_name = model_class.__name__
    table = Table(table_name)
    columns = []

    for field_name, field_type in get_type_hints(model_class).items():
        if field_type is str:
            sql_type = SqlTypes.TEXT
        elif field_type is int:
            sql_type = SqlTypes.INTEGER
        elif field_type is float:
            sql_type = SqlTypes.REAL
        elif inspect.isclass(field_type) and issubclass(field_type, BaseModel):
            sql_type = SqlTypes.TEXT #Store nested models as text.
        else:
            sql_type = SqlTypes.TEXT

        columns.append(Column(field_name, sql_type))

    create_table_sql = create_table(table).columns(*columns).get_sql()

    try:
        cursor = db_connection.cursor()
        cursor.execute(create_table_sql)
        db_connection.commit()
        print(f"Table '{table_name}' created successfully using PyPika.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Example usage:
db_connection = sqlite3.connect("my_database_pypika.db")

create_table_pypika(Paciente, db_connection)

db_connection.close()

#Example with another table.
class Doctor(ModelBase):
  nombre: str
  especialidad: str
  cedula: str

db_connection = sqlite3.connect("my_database_pypika.db")
create_table_pypika(Doctor, db_connection)
db_connection.close()












def guardar_paciente():
    pass

