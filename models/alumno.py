from dataclasses import dataclass      #decorador
from db.session import Db
import sqlalchemy as sa


@dataclass(init=False, repr=True, eq=True)

class Alumno (Db):
    __tablename__ = 'alumnos'
    apellido: str = sa.Column(sa.VARCHAR(200), nullable=True)
    nombre: str = sa.Column(sa.VARCHAR(200), nullable=True)
    nro_doc: str = sa.Column(sa.VARCHAR(200), nullable=True)
    tipo_doc: str = sa.Column(sa.VARCHAR(200), nullable=True)        #uso varchar porque es mas rapido de parsear que detetime
    fecha_nac: str = sa.Column(sa.VARCHAR(200), nullable=True)
    sexo: str = sa.Column(sa.VARCHAR(200), nullable=True)
    legajo: int = sa.Column(sa.Integer, primary_key=True, autoincrement=False)
    fecha_ingreso: str = sa.Column(sa.VARCHAR(200), nullable=True)

     
