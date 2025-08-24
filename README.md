# SySacad 2.0 - Desarrollo de Software
## Integrantes
- López Laszuk Juan Pablo
- Piastrellini Mariano
- Buttini Cristobal
- Sosa Ricardo
- Iriarte López Ana Valentina
- Moya Carlos

SYSACAD 2.0 es un sistema académico desarrollado en Python, diseñado bajo una arquitectura en capas y con un enfoque de desarrollo guiado por pruebas (TDD).

> ⚡ La arquitectura de SYSACAD 2.0 está estructurada en múltiples capas y módulos especializados, que garantizan la separación de responsabilidades:
models - repositories - services - mapping - resources - tests

---

## 📂 Descripcion Modulos Principales del proyecto 

```
SYSACAD 2.0/
├── models/             # Definiciones de tablas como objetos usando a SQLALCHEMY (ORM)
├── repositories/       # Acceso y persistencia en BD (SQLAlchemy)
├── services/           # Lógica de negocio 
├── test/               # Pruebas unitarias (verifican solo la conexion con service)
├── mapping/            # Serialización, deserialización y validación de datos
├── resources/          # Recursos REST que exponen la API (Solicitudes HTTP)
├── db/                 # Configuración de sesión SQLAlchemy
├── config/             # Lectura de variables de entorno (.env)
├── .env                # Variables de Entorno. Contiene la URI de conexión a PostgreSQL
├── requirements.txt    # Dependencias necesarias
└── README.md           # Documentacion principal 
```

## 🔧 Modulos del proyecto

### 1. **models/**

En esta carpeta se definen las **tablas como clases de Python**, utilizando la biblioteca **SQLAlchemy** como ORM (Object Relational Mapper). Cada clase representa una entidad académica (por ejemplo, `Facultad`, `Materia`, `Localidad`) y se mapea a una tabla real de PostgreSQL
* Utiliza `SQLAlchemy` sin usar de `Flask` (mas simple)

### 3. **services/**

* Contiene la **lógica de negocio (que debe hacer)**.
* Lee archivos XML (`ElementTree`) con codificación especial `Windows-1252`.
* Valida, transforma e instancia los modelos para ser guardados por la capa repository.

### 4. **test/**

* Solo se  ** verifica la conexión entre `test → service`**.
* No se valida persistencia ni consultas en la base (No tiene CRUD)

### 5. ** scripts**

Cada entidad tiene un script dedicado dentro de `scripts/`, que:

* Crea las tablas necesarias (si es que no existen, si ya existen solo actualiza el contenido con el metodo cargar de servivce).
* Llama al método `cargar_xml()` para cargar y persistir datos.
---


## **Pasos para la ejecución de la aplicacion **

1. **Crear el entorno virtual en la raiz del proyecto**  
   ➜ `python -m venv venv`

2. **Activar el entorno virtual (necesario para instalar las librerias de requirements.txt )**  
   ➜ `.\venv\Scripts\Activate.ps1`

3. **Instalar las librerías que estan en requirements.txt**  
   ➜ `pip install -r requirements.txt`

**El paso 3 se puede evitar utilizando el script install.ps1**

<img width="159" height="23" alt="image" src="https://github.com/user-attachments/assets/a6c21d32-aac3-4870-bf43-b2227d955035" />

* a- Acceder al script.ps1
* b- Modificar la ruta del entorno virtual si es necesario
* <img width="506" height="22" alt="image" src="https://github.com/user-attachments/assets/2546c7a6-5797-4a7d-b3ba-f9de6a69a2b4" />
* c- Si es necesario modificar la Política de Ejecución a RemoteSigned → permite ejecutar scripts locales sin firmar
* c- Ejecutar el script install.ps1 en la terminal 




5. **Crear un archivo `.env` en la raíz del directorio**  
   ➜ Archivo: `.env`

6. **Usar como modelo el archivo `env-example` y completar en `.env` los datos de conexión a la base de datos**  
   *(usuario, contraseña, nombre de la DB)*

7. **Ejecutar los scripts de carga desde la carpeta `scripts/`**  
   Cada script persiste los datos de un XML distinto.  
   ➜ Para que se creen todas las tablas y se carguen todos los datos, ejecutá cada uno:

   ```bash
   python scripts/facultad_persistencia.py
   python scripts/especialidad_persistencia.py
   python scripts/grado_persistencia.py
   python scripts/materia_persistencia.py
   ...
8. **Se pueden ver las tablas con su contenido usando la terminal de Docker**  
   ➜ Usando la terminal dentro del servidor de DOCKER:

   ```bash
   # Conectarse al usuario
   psql -U sysacad_cristobal -d postgres

   # Listar bases de datos disponibles
   \l

   # Conectarse a la base de datos de trabajo
   \c DEV_SYSACAD

   # Listar todas las tablas dentro de la base actual
   \dt

   # Mostrar el contenido de una tabla específica
   SELECT * FROM nombre_tabla; 
---

## 📅 Mejoras 

>En vez de tener un script de persistencia por archivo o modelo, seria mejor usar un solo script que persista los datos de TODOS los archivos XML. Esto para seguir el principio DRY consiste en que no repitamos bloques de codigo que hacen lo mismo en diferentes partes del proyecto

> Mejorar la importacion de algunos modulos como service y repos
---

## 📚 Tecnologías utilizadas

* **Python 3.13**
* **SQLAlchemy** (ORM)
* **PostgreSQL** como base de datos
* **Archivos XML** con codificación `Windows-1252`
* **Estructura de proyecto en capas** (sin Flask no es cliente-servidor)
* **Docker** (para base de datos local DEV_SYSACAD)
---

## **Pasos para la ejecución**

1. **Crear el entorno virtual**  
   ➜ `python -m venv venv`

2. **Activar el entorno virtual (necesario para instalar las dependencias y librerias necesarias para que se ejecute)**  
   ➜ `.\venv\Scripts\Activate.ps1`

3. **Instalar las librerías que estan en requirements.txt**  
   ➜ `pip install -r requirements.txt`

4. **Crear un archivo `.env` en la raíz del directorio**  
   ➜ Archivo: `.env`

5. **Usar como modelo el archivo `env-example` y completar en `.env` los datos de conexión a la base de datos**  
   *(usuario, contraseña, nombre de la DB)*

6. **Ejecutar los scripts de carga desde la carpeta `scripts/`**  
   Cada script persiste los datos de un XML distinto.  
   ➜ Para que se creen todas las tablas y se carguen todos los datos, ejecutá cada uno:

   ```bash
   python scripts/facultad_persistencia.py
   python scripts/especialidad_persistencia.py
   python scripts/grado_persistencia.py
   python scripts/materia_persistencia.py
   ...
7. **Se pueden ver las tablas con su contenido usando la terminal de Docker**  
   ➜ Usando la terminal dentro del servidor de DOCKER:

   ```bash
   # Conectarse al usuario
   psql -U sysacad_cristobal -d postgres

   # Listar bases de datos disponibles
   \l

   # Conectarse a la base de datos de trabajo
   \c DEV_SYSACAD

   # Listar todas las tablas dentro de la base actual
   \dt

   # Mostrar el contenido de una tabla específica
   SELECT * FROM nombre_tabla; 
---



## ♻ Autor

Cristobal Buttini  Legajo n° 9976
Sosa Ricardp       Legajo n° 10255

