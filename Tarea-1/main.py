import cx_Oracle
from tabulate import tabulate
import csv
import connect, regiones, comunas, vistas, triggers, menu

cursor, connection = connect.iniciar()

#regiones.crearTabla(cursor)
#comunas.crearTabla(cursor)
#regiones.insertarCSV(cursor)
#comunas.insertarCSV(cursor)
#comunas.crearComuna(cursor)
#regiones.crearRegion(cursor)
#vistas.vistaRegiones(cursor)
#comunas.aumentarCasos(cursor)
#comunas.disminuirCasos(cursor)
#comunas.verCasos(cursor)
#comunas.verTodos(cursor)
#regiones.verCasos(cursor)
#regiones.verTodos(cursor)
#regiones.positividadRegional(cursor)
#regiones.top5Regiones(cursor)
#comunas.top5Comunas(cursor)
#regiones.combinarRegiones(cursor)
#comunas.combinarComunas(cursor)
menu.menu(cursor)

connect.terminar(connection)
