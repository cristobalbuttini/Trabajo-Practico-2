import csv
from models.alumno import Alumno

class AlumnoService:
    def __init__(self, repository):
        self.repository = repository

    def importar_csv(self, path_csv: str, batch_size: int = 10):
        """
        Lee un archivo CSV y persiste los alumnos en lotes.
        :param path_csv: Ruta al archivo CSV
        :param batch_size: Tamaño del lote para inserción masiva
        """
        buffer = []
        with open(path_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for fila in reader:
                alumno = Alumno(
                    apellido=fila["apellido"],
                    nombre=fila["nombre"],
                    nro_doc=fila["nro_documento"],
                    tipo_doc=fila["tipo_documento"],
                    fecha_nac=fila["fecha_nacimiento"],  # VARCHAR, no se castea
                    sexo=fila["sexo"],
                    legajo=int(fila["nro_legajo"]),
                    fecha_ingreso=fila["fecha_ingreso"]  # VARCHAR, no se castea
                )
                buffer.append(alumno)

                if len(buffer) >= batch_size:
                    self.repository.bulk_insert(buffer)
                    buffer = []

            # Insertar lo que queda en el buffer
            if buffer:
                self.repository.bulk_insert(buffer)
