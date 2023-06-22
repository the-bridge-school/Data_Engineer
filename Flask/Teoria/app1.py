from flask import Flask


# Flask es una instancia WSGI y por eso la clase la instanciamos en una 
# variable app

app = Flask(__name__) # Para crear dicha instancia, debemos pasar como 
                      # primer argumento el nombre del módulo o paquete 
                      # de la aplicación. Para estar seguros de ello, 
                      # utilizaremos la palabra reservada __name__. 
                      # Esto es necesario para que Flask sepa, por ejemplo, 
                      # donde encontrar las plantillas de nuestra aplicación 
                      # o los ficheros estáticos.

@app.route('/', methods=['GET'])         # @app es un decorador que nos ayuda a indicarle a python
                        # que route pertenece a flask.

def hello_world():      # Función de python que realiza la magia. 
    return 'Hello, World!'

# Nota 1. importante no nombrar el archivo como flask.py porque puede crear un 
# conflicto con Flask

app.run(debug=True)

# Nota 2. si queremos ejecutar nuestra app sin pulsar el "Play" hay que hacer unas pequeñas
# modificaciones en el virtualenv

# En Linux/Mac se encuentra en env/bin/activate. Al final del fichero añadimos lo siguiente:
# export FLASK_APP="run.py"

# En Windows se encuentra en env\Scripts\activate.bat. Al final del fichero añadimos lo siguiente:
# set "FLASK_APP=run.py"

# Nota 2.1 Se tiene que desactivar y volver a activar para que los cambios se tengan en cuenta

# Una vez realizado estos cambios en la terminal se ejecuta el comando
# flask app1

# Nota 3 no usar el debug en Producción.