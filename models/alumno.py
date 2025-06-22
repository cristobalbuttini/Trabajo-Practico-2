from dataclasses import dataclass     
from db.session import Db
import sqlalchemy as sa


@dataclass(init=False, repr=True, eq=True)

class Alumno (Db):
    __tablename__ = 'alumnos'
    apellido: str = sa.Column(sa.VARCHAR(20), nullable=True)
    nombre: str = sa.Column(sa.VARCHAR(20), nullable=True)
    nro_doc: str = sa.Column(sa.VARCHAR(20), nullable=True)
    tipo_doc: str = sa.Column(sa.VARCHAR(20), nullable=True)        #uso varchar porque es mas rapido de parsear que datetime
    fecha_nac: str = sa.Column(sa.VARCHAR(20), nullable=True)
    sexo: str = sa.Column(sa.VARCHAR(1), nullable=True)
    legajo: int = sa.Column(sa.Integer, primary_key=True, autoincrement=False)
    fecha_ingreso: str = sa.Column(sa.VARCHAR(20), nullable=True)

     
