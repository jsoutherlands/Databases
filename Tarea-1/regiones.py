import re
import csv

def crearTabla(cursor):
	print("Creando Tabla Regiones...")
	cursor.execute(
		"""
			CREATE TABLE CASOS_POR_REGION(
		    ID_COMUNA INTEGER NOT NULL,
		    ID_REGION INTEGER NOT NULL,
		    NOMBRE_REGION VARCHAR2(50) NOT NULL,
		    CASOS_CONFIRMADOS INTEGER NOT NULL,
		    POBLACION INTEGER NOT NULL,
		    CONSTRAINT PK_REGION PRIMARY KEY (ID_REGION),
		    CONSTRAINT FK_COMUNA FOREIGN KEY (ID_COMUNA) REFERENCES CASOS_POR_COMUNA(ID_COMUNA)
			)
		"""
		)
	print("Tabla Regiones creada.")

def insertarCSV(cursor):
	csvRegiones = open("RegionesComunas.csv", "r", encoding='utf-8')
	csvRegiones = csv.reader(csvRegiones)
	next(csvRegiones)
	csvComunas = open("CasosConfirmadosPorComuna.csv", "r", encoding='utf-8')
	csvComunas = csv.reader(csvComunas)
	next(csvComunas)
	print("Ingresando archivo \"RegionesComunas.csv\" a CASOS_POR_REGION...")
	print("Ingresando archivo \"CasosConfirmadosPorComuna.csv\" a CASOS_POR_REGION...")
	listaComunas = []
	for comunas in csvComunas:
		listaComunas.append((int(comunas[1]), int(comunas[2]), int(comunas[3])))
	for linea in csvRegiones:
		nombreRegion = linea[0]
		codigoRegion = int(linea[1])
		codigoComuna = int(linea[2])
		for linea2 in listaComunas:
			if linea2[0] == codigoComuna:
				casosConfirmados = linea2[2]
				poblacion = linea2[1]
		print(codigoRegion, codigoComuna, nombreRegion, casosConfirmados, poblacion)
		cursor.execute(
			"""
			INSERT INTO CASOS_POR_REGION VALUES (:1, :2, :3, :4, :5)
			""", [codigoRegion, codigoComuna, nombreRegion, casosConfirmados, poblacion]
			)
	print("Inserción finalizada.")

def crearRegion(cursor):
	print("Al crear una región, se debe sí o sí inventar una nueva comuna.\n Esta comuna llevará el nombre de la región.")
	codigoRegion = input("Ingresa el código de la región: ")
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
		codigoComuna = int(codigoRegion + "101")
		casosConfirmados = input("Ingresa la cantidad de casos activos de la región: ")
		poblacion = input("Ingresa la cantidad de casos activos de la región: ")
		cursor.execute(
			"""
			INSERT INTO CASOS_POR_COMUNA VALUES (:1, :2, :3, :4)
			""", [codigoComuna, nombreRegion, casosConfirmados, poblacion]
			)
		cursor.execute(
			"""
			INSERT INTO CASOS_POR_REGION VALUES (:1, :2, :3, :4, :5)
			""", [codigoRegion, codigoComuna, nombreRegion, casosConfirmados, poblacion])
		print("Región -y comuna inicial- creada correctamente.")
	else:
		print("¡Esta región ya existe! Inténtalo nuevamente.")

def verCasos(cursor):
	codigoRegion = input("Ingrese el código de la región que desea ver: ")
	cursor.execute(
		"""
		SELECT ID_REGION FROM CASOS_POR_REGION WHERE ID_REGION = :1
		""", [codigoRegion]
		)
	existe = cursor.fetchone()
	if existe == None:
		print("La región que buscas no existe. Inténtalo nuevamente.")
	else:
		cursor.execute(
			"""
			SELECT ID_REGION, NOMBRE_REGION, SUM(CASOS_CONFIRMADOS) AS CASOS_CONFIRMADOS FROM CASOS_POR_REGION GROUP BY ID_REGION, NOMBRE_REGION
			"""
			)
		datos = cursor.fetchall()
		print("REGIÓN 		CASOS CONFIRMADOS")
		for region in datos:
			if str(codigoRegion) == str(region[0]):
				print(region[1] + "		" + str(region[2]))

def verTodos(cursor):
	cursor.execute(
		"""
		SELECT NOMBRE_REGION, SUM(CASOS_CONFIRMADOS) AS CASOS_CONFIRMADOS FROM CASOS_POR_REGION GROUP BY ID_REGION, NOMBRE_REGION
		"""
		)
	datos = cursor.fetchall()
	if datos != None:
		print("REGIÓN CASOS CONFIRMADOS")
		for region in datos:
			print(region[0] + "	" + str(region[1]))
	else:
		print("No existen regiones para mostrar.")
