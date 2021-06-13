import connect, regiones, comunas, vistas, triggers

def menu(cursor):
	print("Bienvenid@ a la Base de Datos COVID-21.\nIngrese un número del siguiente menú para continuar:")
	print("	1 	| Crear una comuna.")
	print("	2 	| Crear una región.")
	print("	3	| Ver casos totales de una comuna.")
	print("	4	| Ver casos totales de una región.")
	print("	5 	| Ver casos totales de todas las comunas.")
	print("	6	| Ver casos totales de todas las regiones.")
	print("	7	| Agregar casos nuevos a una comuna.")
	print("	8	| Eliminar casos nuevos a una comuna.")
	print("	9	| Combinar comunas.")
	print("	10	| Combinar regiones.")
	print("	11	| Top 5 comunas con más porcentaje de casos según su población.")
	print("	12 	| Top 5 regiones con más porcentaje de casos según su población.")
	print("	13	| Guardar y salir.")
	numeroMenu = int(input("Ingrese opción: "))
	while numeroMenu != 13:
		if numeroMenu == 1:
			comunas.crearComuna(cursor)
		elif numeroMenu == 2:
			regiones.crearRegion(cursor)
		elif numeroMenu == 3:
			comunas.verCasos(cursor)
		elif numeroMenu == 4:
			regiones.verCasos(cursor)
		elif numeroMenu == 5:
			comunas.verTodos(cursor)
		elif numeroMenu == 6:
			regiones.verTodos(cursor)
		elif numeroMenu == 7:
			comunas.aumentarCasos(cursor)
		elif numeroMenu == 8:
			comunas.disminuirCasos(cursor)
		elif numeroMenu == 9:
			comunas.combinarComunas(cursor)
		elif numeroMenu == 10:
			regiones.combinarRegiones(cursor)
		elif numeroMenu == 11:
			comunas.top5Comunas(cursor)
		elif numeroMenu == 12:
			regiones.top5Regiones(cursor)
		elif numeroMenu == 13:
			numeroMenu = 13
		regiones.positividadRegional(cursor)
		input("Pulsa ENTER para continuar... ")
		print("	1 	| Crear una comuna.")
		print("	2 	| Crear una región.")
		print("	3	| Ver casos totales de una comuna.")
		print("	4	| Ver casos totales de una región.")
		print("	5 	| Ver casos totales de todas las comunas.")
		print("	6	| Ver casos totales de todas las regiones.")
		print("	7	| Agregar casos nuevos a una comuna.")
		print("	8	| Eliminar casos nuevos a una comuna.")
		print("	9	| Combinar comunas.")
		print("	10	| Combinar regiones.")
		print("	11	| Top 5 comunas con más porcentaje de casos según su población.")
		print("	12 	| Top 5 regiones con más porcentaje de casos según su población.")
		print("	13	| Guardar y salir.")
		numeroMenu = int(input("Ingrese opción: "))
	print("\nSaliendo...\n")
