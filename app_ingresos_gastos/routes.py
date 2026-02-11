from app_ingresos_gastos import app
from flask import render_template,request,redirect
import csv 
from datetime import date

@app.route("/")
def index():
    datos = []
    fichero = open("app_ingresos_gastos/data/movimientos.csv","r")
    lectura = csv.reader(fichero, delimiter=",",quotechar='"')
    for item in lectura:
        datos.append(item)
    """
    datos = [
        {"fecha":"01/09/2025","concepto":"Salario","monto":1800},
        {"fecha":"15/09/2025","concepto":"Compras de Alimentos","monto":-250},
        {"fecha":"30/09/2025","concepto":"Compra de Ropa","monto":-150}
    ]
    """

    return render_template("index.html", title=" Lista",lista = datos)

@app.route("/new",methods=["GET","POST"])
def new():
    if request.method == "POST":
        
        comprobar_errores = validar_formulario(request.form)
        if comprobar_errores:
            return render_template("new.html", title="Registro", titulo="Registro",boton="Guardar",error=comprobar_errores,dataform = request.form)

        else:
            fichero = open("app_ingresos_gastos/data/movimientos.csv","a",newline="")
            lectura = csv.writer(fichero, delimiter=",", quotechar='"')
            lectura.writerow([request.form["fecha"],request.form["concepto"],request.form["monto"]])
            fichero.close()
        
        return redirect("/")
    
    else:
        return render_template("new.html",title=" Registro",titulo="Registro",boton="Guardar",dataform = {})

@app.route("/delete/<int:id>")
def delete(id):
    return render_template("delete.html",title="Borrar")

@app.route("/update/<int:id>")
def update(id):
    return render_template("update.html",title="Actualizar",titulo="Actualización",boton="Actualizar")


def validar_formulario(datos_formulario):
    hoy = str(date.today())
    errores = []
    if datos_formulario["fecha"] > hoy:
        errores.append("La fecha no puede ser mayor que la actual")
    if datos_formulario["concepto"] == "":
        errores.append("El concepto no puede ir vacío")
    if datos_formulario["monto"] == "" or float(datos_formulario["monto"]) == 0:
        errores.append("El monto debe ser diferente de 0 o no estar vacío")
            
    return errores