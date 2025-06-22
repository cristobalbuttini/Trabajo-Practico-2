import time
from db.session import get_session
from repositories.alumno_repositorio import AlumnoRepository
from services.alumno_service import AlumnoService

def main():
    # Inicializar sesión, repositorio y servicio
    session = get_session()
    repo = AlumnoRepository(session)
    service = AlumnoService(repo)

    # Medir tiempo de ejecución
    inicio = time.perf_counter()
    service.importar_csv("csv_data/alumnos.csv", batch_size=10)
    fin = time.perf_counter()

    print(f"✅ Importación finalizada.")
    print(f"⏱️ Tiempo total: {fin - inicio:.2f} segundos.")

if __name__ == "__main__":
    main()
