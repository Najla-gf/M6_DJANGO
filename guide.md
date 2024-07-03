# Guía de Configuración y Comandos

## Paso 1: Crear y activar el entorno virtual
```bash
python -m venv nombre_entorno  # Crea un entorno virtual con el nombre especificado
source nombre_entorno/Scripts/activate  # Activa el entorno virtual en Windows
```

## Paso 2: Ver las dependencias e instalar lo necesario
```bash
pip list  # Lista las dependencias instaladas actualmente en el entorno virtual
pip install django  # Instala Django en el entorno virtual
```

## Paso 3: Instalar driver de la base de datos (PostgreSQL) en nuestro entorno virtual
```bash
pip install psycopg2   # Instala el driver de PostgreSQL
pip install --upgrade pip  # Actualiza pip a la última versión
pip list  # Verifica las dependencias instaladas
```

## Paso 4: Crear proyecto e ingresar a la carpeta
```bash
django-admin startproject nombre_proyecto  # Crea un nuevo proyecto Django con el nombre especificado
cd nombre_proyecto  # Entra en la carpeta del proyecto
```

## Paso 4.5: Crear la base de datos
### Base de Datos (Terminal Bash)
```sql
CREATE DATABASE nombre_bbdd;  # Crea una nueva base de datos con el nombre especificado
\l  # Lista todas las bases de datos existentes
\c nombre_bbdd  # Conéctate a la base de datos especificada
\q  # Sal de la sesión de la base de datos
```

### Vincular en `settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Utiliza el backend de PostgreSQL
        'NAME': 'nombre_bbdd',  # Nombre de la base de datos
        'USER': 'postgres',  # Usuario de la base de datos
        'PASSWORD': 'Admin1234',  # Contraseña de la base de datos
        'HOST': '127.0.0.1',  # Dirección del host de la base de datos
        'PORT': '5432',  # Puerto de conexión de la base de datos
    }
}
```

```python
PORT: '3606'  # Puerto para mySQL 
```

## Paso 5: Agregar app al proyecto
```bash
python manage.py startapp nombre_aplicacion  # Crea una nueva aplicación Django con el nombre especificado
```

### En `settings.py`
```python
INSTALLED_APPS = [
    '...',
    'nombre_aplicacion',  # Agrega la nueva aplicación a la lista de aplicaciones instaladas
]
```

## Paso 6: TEMPLATES
1. Crear la carpeta `templates` en la app.
2. Crear los archivos HTML con estructura básica.
3. Crear un método que despliega el HTML.
4. Crear una ruta que enlace a `views.py` de la app.

## Paso 7: MODELOS
1. Crear el modelo en `models.py`.
2. Agregar al `admin.py`.
    ```python
    from .models import Nombre_Modelo  # Importa el modelo creado
    admin.site.register(Nombre_Modelo)  # Registra el modelo en el administrador de Django
    ```

## Crear un superusuario
```bash
python manage.py createsuperuser  # Crea un nuevo superusuario para acceder al administrador de Django
```
- **Username:** (leave blank to use 'najla')
- **Email address:** najla.gatica@gmail.com
- **Password:** Admin1234
- **Password (again):** Admin1234

```plaintext
Superuser created successfully.
```

## Paso 8: Ejecutar las migraciones
```bash
python manage.py makemigrations  # Prepara las migraciones de base de datos
python manage.py migrate  # Aplica las migraciones de base de datos
```

### Revisar en base de datos (Terminal Bash)
```sql
\d  # Verifica que el modelo creado esté en la lista de tablas de la base de datos
```

## Ejecutar el servidor
```bash
python manage.py runserver  # Inicia el servidor de desarrollo de Django
```

## Conocer todas las migraciones y saber cuales se han ejecutado en la BD
```bash
python manage.py showmigrations  # Muestra todas las migraciones disponibles
python manage.py showmigrations nombre_aplicacion  # Muestra las migraciones específicas de la aplicación
```

## Revertir una migración específica
```bash
python manage.py migrate nombre_aplicacion 0001_initial  # Revertir a una migración específica
```

## Entrar a la shell de django desde la terminal
```bash
python manage.py shell  # Inicia una sesión interactiva de Django
```
```
