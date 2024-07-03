# Comandos DJANGO

## Crear entorno virtual
```bash
python -m venv vdjango
```
- `python -m venv`: Instrucción para crear un entorno virtual.
- `vdjango`: Nombre del entorno virtual.

## Activación y desactivación de entorno virtual
```bash
source vdjango/Scripts/activate  # Funciona en bash
```
Para salir del entorno virtual:
```bash
deactivate
```

## Comprobaciones e instalación de módulos
```bash
pip list            # Ver las dependencias instaladas en el entorno
pip install django  # Instalar Django en el entorno virtual
```

## Creación de proyecto
```bash
django-admin startproject myFirstApp  # Crea el proyecto "myFirstApp"
```

## Correr el proyecto
```bash
cd myFirstApp               # Acceder a la carpeta del proyecto
python manage.py runserver  # Correr el servidor de desarrollo
```

## Creación de aplicaciones
```bash
python manage.py startapp login  # Crear la aplicación "login"
```

## Vinculando aplicación al archivo `settings.py`
En el archivo `settings.py`, añade la aplicación a `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    '<Nombre de la aplicacion>',
]
```

## Crear e instalar un archivo de dependencias
Para crear un archivo `requirements.txt` con las dependencias del proyecto:
```bash
pip freeze > requirements.txt
```
Para instalar las dependencias del proyecto desde `requirements.txt`:
```bash
pip install -r requirements.txt
```
```