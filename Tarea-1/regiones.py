from tabulate import tabulate
import csv

def crearTabla(cursor):
	print("Creando Tabla Regiones...")
	cursor.execute(
		"""
			CREATE TABLE CASOS_POR_REGION(
			ID_REGION INTEGER NOT NULL,
			NOMBRE_REGION VARCHAR2(50) NOT NULL,
			CASOS_CONFIRMADOS INTEGER NOT NULL,
			POBLACION INTEGER NOT NULL,
			CONSTRAINT PK_REGION PRIMARY KEY (ID_REGION)
		    )
		"""
		)
	print("Tabla Regiones creada.")

def insertarCSV(cursor):
	csvRegiones = open("RegionesComunas.csv", "r", encoding='utf-8')
	csvRegiones = csv.reader(csvRegiones)
	next(csvRegiones)

	for linea in csvRegiones:
		nombreRegion = linea[0]
		codigoRegion = int(linea[1])
		try:
			cursor.execute(
				"""
				INSERT INTO CASOS_POR_REGION VALUES (:1,:2,0,0)
				""", [codigoRegion, nombreRegion]
				)
		except Exception as err:
			continue

def crearRegion(cursor):
	codigoRegion = input("Ingresa el código de la nueva región: ")
	if len(str(codigoRegion)) > 2:
		print("El codigo de la region es demasiado grande. Inténtelo nuevamente.")
		return
	cursor.execute(
		"""
		SELECT ID_REGION FROM CASOS_POR_REGION WHERE ID_REGION = :1
		""", [codigoRegion]
		)
	existe = cursor.fetchone()
	if existe == None:
		nombreRegion = input("Ingresa el nombre que llevará la región: ")
		cursor.execute(
			"""
			INSERT INTO CASOS_POR_REGION VALUES (:1, :2, 0, 0)
			""", [codigoRegion, nombreRegion])
		print("Región creada correctamente.")
	else:
		print("¡Esta región ya existe! Inténtalo nuevamente.")

def verCasos(cursor):
	codigoRegion = input("Ingrese el código de la región que desea ver: ")
	try:
		cursor.execute(
			"""
			SELECT NOMBRE_REGION, CASOS_CONFIRMADOS FROM CASOS_POR_REGION WHERE ID_REGION = :1
			""", [codigoRegion]
			)
		datos = cursor.fetchall()
		var = datos[0][0]
	except Exception as err:
		print("¡Error! La región no existe.")
	else:
		print(tabulate(datos, ['REGION', "CASOS CONFIRMADOS"], tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))
	finally:
		print("Operación finalizada...")

def verTodos(cursor):
	try:
		cursor.execute(
		"""
		SELECT ID_REGION, NOMBRE_REGION, CASOS_CONFIRMADOS FROM CASOS_POR_REGION
		"""
		)
		datos = cursor.fetchall()
		var = datos[0][0]
	except Exception as err:
		print("No existen regiones para mostrar.")
	else:
		print(tabulate(datos, ['REGIONES', "CASOS CONFIRMADOS"], tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))
	finally:
		print("Operación finalizada...")

def top5Regiones(cursor):
	try:
		cursor.execute(
			"""
				SELECT NOMBRE_REGION, ROUND(((CASOS_CONFIRMADOS/POBLACION)*100),2) AS POSITIVIDAD_REGIONAL FROM CASOS_POR_REGION ORDER BY POSITIVIDAD_REGIONAL DESC
			""")
		datos = cursor.fetchmany(5)
		var = datos[0][0]
	except Exception as err:
		print("No es posible mostrar el top 5 dado que no existen regiones.")
	else:
		print(tabulate(datos, ["REGION","POSITIVIDAD REGIONAL [%]"], tablefmt='fancy_grid', stralign='center'))

def positividadRegional(cursor):
	try:
		cursor.execute(
			"""
				SELECT ID_REGION, NOMBRE_REGION, ROUND(((CASOS_CONFIRMADOS/POBLACION)*100),2) AS POSITIVIDAD_REGIONAL FROM CASOS_POR_REGION
			""")
		datos = cursor.fetchall()
		var = datos[0][0]
	except Exception as err:
		return
	else:
		for dato in datos:
			if dato[2] > 15:
				print("La región de {} sobrepasa el límite de positividad regional en un {}% y será eliminada a continuación.".format(dato[1], str(dato[2]-15)))
				cursor.execute(
					"""
						DELETE FROM CASOS_POR_REGION
						WHERE ID_REGION = :1
					""", [dato[0]])


def combinarRegiones(cursor):
	region1 = int(input("Ingrese el código de la región a combinar: "))
	region2 = int(input("Ingrese el código de la otra región a combinar: "))
	cursor.execute(
		"""
			SELECT * FROM CASOS_POR_REGION WHERE ID_REGION IN (:1,:2)
		""",[region1, region2]
		)
	row = cursor.fetchall()
	if len(row) != 2:
		print("Error: Una o ambas regiones no existen. Inténtalo nuevamente.")
		print("Operación finalizada.")
		return
	codigoRegion = int(input("Ingrese una de las siguientes opciones:\n 1 | Conservar el código de la región 1.\n 2 | Conservar el código de la región 2.\n Opción: "))
	if codigoRegion == 1:
		codigoRegion = region1
		oldRegion = region2
	elif codigoRegion == 2:
		codigoRegion = region2
		oldRegion = region1
	else:
		print("Opción no válida.")
		print("Operación finalizada...")
		return
	nombreRegion = input("Ingrese nuevo nombre de la región: ")
	cursor.execute(
		"""
			UPDATE CASOS_POR_COMUNA
			SET ID_REGION = :1
			WHERE ID_REGION = :2
		""", [codigoRegion, oldRegion]
		)
	cursor.execute(
		"""
			SELECT SUM(CASOS_CONFIRMADOS) AS TODOS_CASOS, SUM(POBLACION) AS TODOS_POBLACION
			FROM CASOS_POR_COMUNA
			WHERE ID_REGION = :1
			GROUP BY ID_REGION
		""", [codigoRegion]
		)
	casosConfirmados, poblacion = cursor.fetchone()
	print(nombreRegion, int(casosConfirmados), int(poblacion), codigoRegion)
	cursor.execute(
		"""
			UPDATE CASOS_POR_REGION
			SET NOMBRE_REGION = :1,
				CASOS_CONFIRMADOS = :2,
				POBLACION = :3
			WHERE ID_REGION = :4
		""", [nombreRegion, int(casosConfirmados), int(poblacion), codigoRegion]
		)
	cursor.execute(
		"""
			DELETE FROM CASOS_POR_REGION
			WHERE ID_REGION = :1
		""", [oldRegion]
		)
	print("Operación finalizada...")
