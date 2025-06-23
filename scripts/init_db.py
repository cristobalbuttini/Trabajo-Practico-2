from db.session import engine, Db
import models.alumno  # ¡importa explícitamente el modelo!

if __name__ == "__main__":
    Db.metadata.create_all(bind=engine)
    print("✅ Tablas creadas en DEV_SYSACAD_2")
