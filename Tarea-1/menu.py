
def menu(cursor):
	print("Bienvenid@ a la Base de Datos COVID-21. Ingrese un número del siguiente menú para continuar:")
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
	print("	13	| Salir.")
	numeroMenu = input()
	while numeroMenu != 13:
		print("Operación finalizada. ¿Desea continuar? (SI/NO)")
		sino = input()
		if sino == "SI":
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
			print("	13	| Salir.")
			numeroMenu = input()
		elif sino == "NO":
			print("Saliendo de la Base de Datos...")
			numeroMenu = 13

