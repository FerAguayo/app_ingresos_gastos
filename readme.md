## English

# Income and Expenses Web Application with Flask

A Python application built with the Flask framework.

## Installation

Create a Python virtual environment, activate it, and run:
```bash
pip install -r requirements.txt
```

The library used is https://flask.palletsprojects.com/en/stable/

## Running the Application

To start the Flask server, follow these steps depending on your platform:

**On Windows (cmd or PowerShell):**
```bash
set FLASK_APP=main.py
```

**On Mac or Linux terminal:**
```bash
export FLASK_APP=main.py
```

Once the environment variable is set, start the server:
```bash
flask --app main run
```

## IMPORTANT

This is a development server. Please do not use it in production.

## Changing Ports

Flask normally runs on localhost through port 5000. If you need to use a different port, add the following parameter:
```bash
flask --app main run -p "your_port_number"
```

## Enabling Debug Mode

When editing your code, you normally need to restart the server for changes to take effect. Debug mode solves this by applying changes in real-time:
```bash
flask --app main --debug run
```

#
## Español

# Aplicación web de Ingresos y gastos con Flask

Programa hecho en python con el framework Flask

# Instalación

-Crear un entorno en python, actívalo y ejecutar el comando
```bash
pip install -r requirements.txt
```
La librería utilizada es https://flask.palletsprojects.com/es/stable/

# Ejecución del programa

Para iniciar el servidor flask tendremos que hacer lo siguiente dependiendo de la plataforma:

-En cmd o powershell desde windows:

```bash
set FLASK_APP=main.py
```

-Desde la terminal de comandos de mac o linux:

```bash
export FLASK_APP=main.py
```

Una vez exportado el parámetro debemos ejecutar el servidor:

```bash
flask --app main run
```

## IMPORTANTE:
Esto es un servidor de desarrollo, por favor no utilizarlo en producción.

## Cambio de puertos

Flask se ejecuta normalmente en localhost entrando por el puerto 5000, si por algún casual tienes el puerto usado con el siguiente parámetro lo cambias:

```bash
 flask --app main run -p "puerto_que_quieras_añadir" 
 ```

## Activar el modo debug

Cuando editamos algún parámetro en nuestro programa debemos de cerrar el server y volver a cargarlo, con el modo debug, eso se soluciona y aplica cambios en directo,
el modo se aplica con el siguiente parámetro:

```bash
flask --app main --debug run 
```
