# Tutorial de Flask

## Funcionalidades del miniblog

El miniblog a desarrollar tendrá las siguientes características:

* Existirán dos tipos de usuario: administradores e invitados.
* Un usuario administrador puede añadir, modificar y eliminar entradas del blog.
* Los usuarios invitados pueden registrarse en el blog para comentar las diferentes entradas.
* Un usuario administrador puede crear, modificar, eliminar y listar usuarios, además de poder asignarles el rol de administrador.


* Mi primera aplicación Flask
* Plantillas para las páginas HTML
* Formularios en Flask
* Login en Flask
* Base de datos: SQLAlchemy
* Estructura de un proyecto con Flask. Blueprints
* Parámetros de configuración Flask
* Manejo de errores y excepciones
* Logs en Flask
* Seguridad en las vistas
* Actualizar BBDD SQLAlchemy
* Test con Flask
* Las consultas de BBDD
* Emails con Flask
* Fechas en Flask
* Ficheros en Flask
* Desplegar una aplicación Flask en producción con Nginx + Gunicorn


### Variables de entorno

Para que el miniblog funcione debes crear las siguientes variables de entorno:

#### Linux/Mac

    export FLASK_APP="run.py"
    export FLASK_ENV="development"

#### Windows

    set "FLASK_APP=run.py"
    set "FLASK_ENV=development"
    
> Mi recomendación para las pruebas es que añadas esas variables en el fichero "activate" o "activate.bat"
> si estás usando virtualenv
 
### Instalación de dependencias

En el proyecto se distribuye un fichero (requirements.txt) con todas las dependencias. Para instalarlas
basta con ejectuar:

    pip install -r requirements.txt

## Ejecución con el servidor que trae Flask

Una vez que hayas descargado el proyecto, creado las variables de entorno y descargado las dependencias,
puedes arrancar el proyecto ejecutando:

    flask run
