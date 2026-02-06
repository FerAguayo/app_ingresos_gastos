#ejemplos de lectura de archivos cvs con python

""" Nos muestra el csv tal cual, en listado:
        01/01/2026,Salario,1600
        05/01/2026,Ropa,-150
        10/01/2026,Compras Alimentos,-200

with open("app_ingresos_gastos/data/movimientos.csv","r") as resultado:
    lectura = resultado.read()
    print(lectura)
"""

"""  Nos muestra el csv como una lista:
        ['01/01/2026,Salario,1600\n', '05/01/2026,Ropa,-150\n', '10/01/2026,Compras Alimentos,-200\n']

resultado = open("app_ingresos_gastos/data/movimientos.csv","r")
lectura = resultado.readlines()
print(lectura)
"""

""" Nos muestra el csv como lista de listas(lol):
        ['01/01/2026', 'Salario', '1600']
        ['05/01/2026', 'Ropa', '-150']
        ['10/01/2026', 'Compras Alimentos', '-200']

import csv 
mifichero = open("app_ingresos_gastos/data/movimientos.csv","r")
lectura = csv.reader(mifichero, delimiter=",",quotechar='"')
for items in lectura:
    print(items)
"""