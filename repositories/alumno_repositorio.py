class AlumnoRepository:
    def __init__(self, session):
        self.session = session

    def bulk_insert(self, alumnos: list):
        """
        Inserta una lista de objetos Alumno utilizando una operación masiva.
        :param alumnos: Lista de instancias de Alumno
        """
        self.session.bulk_save_objects(alumnos)
        self.session.commit()
