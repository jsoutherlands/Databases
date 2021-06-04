import cx_Oracle
import re
import csv
import connect, regiones, comunas, vistas, triggers

cursor, connection = connect.iniciar()

#regiones.crearTabla(cursor)
#comunas.crearTabla(cursor)

#comunas.crearComuna(cursor)
#regiones.crearRegion(cursor)
#comunas.insertarCSV(cursor)
#regiones.insertarCSV(cursor)
#vistas.vistaRegiones(cursor)
#comunas.verCasos(cursor)
regiones.verCasos(cursor)
#regiones.verTodos(cursor)
connect.terminar(connection)