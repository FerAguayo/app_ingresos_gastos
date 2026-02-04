# Aplicación web de Ingresos y gastos con Flask

Programa hecho en python con el framework Flask

# Instalación

-Crear un entorno en python, actívalo y ejecutar el comando
```
pip install -r requirements.txt
```
La librería utilizada es https://flask.palletsprojects.com/en/stable/

# Ejecución del programa

Para iniciar el servidor flask tendremos que hacer lo siguiente dependiendo de la plataforma:

-En cmd o powershell desde windows:

```set FLASK_APP=main.py```

-Desde la terminal de comandos de mac o linux:

```export FLASK_APP=main.py```

Una vez exportado el parámetro debemos ejecutar el servidor:

```flask --app main run```

## IMPORTANTE:
Esto es un servidor de desarrollo, por favor no utilizarlo en producción.

## Cambio de puertos

Flask se ejecuta normalmente en localhost entrando por el puerto 5000, si por algún casual tienes el puerto usado con el siguiente parámetro lo cambias:

``` flask --app main run -p "puerto que quieras añadir" ```

## Activar el modo debug

Cuando editamos algún parámetro en nuestro programa debemos de cerrar el server y volver a cargarlo, con el modo debug, eso se soluciona y aplica cambios en directo,
el modo se aplica con el siguiente parámetro:

```flask --app main --debug run ```