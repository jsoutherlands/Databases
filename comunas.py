import re
import csv

def crearTabla(cursor):
	print("Creando Tabla Comunas...")
	cursor.execute(
		"""
			CREATE TABLE CASOS_POR_COMUNA(
			    ID_COMUNA INTEGER NOT NULL,
			    NOMBRE_COMUNA VARCHAR2(50) NOT NULL,
			    CASOS_CONFIRMADOS INTEGER NOT NULL,
			    POBLACION INTEGER NOT NULL,
			    CONSTRAINT PK_COMUNA PRIMARY KEY (ID_COMUNA)
		    )
		"""
		)
	print("Tabla Regiones creada.")

def aumentarCasos(cursor):
	comuna = int(input("Ingrese el código de la comuna: "))
	nuevos = int(input("Ingrese casos nuevos: "))
	cursor.execute(
		"""
		SELECT ID_COMUNA FROM CASOS_POR_COMUNA WHERE ID_COMUNA = :1
		""", [comuna]
		)
	row = cursor.fetchone()
	if row == None:
		print("La comuna no existe. Intente nuevamente.")
	else:
		cursor.execute(
			"""
				UPDATE CASOS_POR_COMUNA
				SET CASOS_CONFIRMADOS = CASOS_CONFIRMADOS + :1
				WHERE ID_COMUNA = :2
			""", [nuevos, comuna]
			)
		cursor.execute(
			"""
				UPDATE CASOS_POR_REGION
				SET CASOS_CONFIRMADOS = CASOS_CONFIRMADOS + :1
				WHERE ID_COMUNA = :2
			""", [nuevos, comuna]
			)
		print("Agregación de casos nuevos exitosa.")

def disminuirCasos(cursor):
	comuna = int(input("Ingrese el código de la comuna: "))
	nuevos = int(input("Ingrese casos a eliminar: "))
	cursor.execute(
		"""
		SELECT ID_COMUNA FROM CASOS_POR_COMUNA WHERE ID_COMUNA = :1
		""", [comuna]
		)
	row = cursor.fetchone()
	if row == None:
		print("La comuna no existe. Intente nuevamente.")
	else:
		cursor.execute(
			"""
				UPDATE CASOS_POR_COMUNA
				SET CASOS_CONFIRMADOS = CASOS_CONFIRMADOS - :1
				WHERE ID_COMUNA = :2
			""", [nuevos, comuna]
			)
		cursor.execute(
			"""
				UPDATE CASOS_POR_REGION
				SET CASOS_CONFIRMADOS = CASOS_CONFIRMADOS - :1
				WHERE ID_COMUNA = :2
			""", [nuevos, comuna]
			)
		print("Disminución de casos exitosa.")

def crearComuna(cursor):
	codigo = input("Ingrese codigo de comuna (DEBE tener entre 4 y 5 números, y los dos primeros deben tener el codigo de la region): ")
	cursor.execute(
		"""
		SELECT ID_COMUNA FROM CASOS_POR_COMUNA WHERE ID_COMUNA = :1
		""", [codigo]
		)
	row = cursor.fetchone()
	if row == None:
		nombre = input("Ingrese el nombre de la comuna: ")
		poblacion = input("Ingrese población actual: ")
		casosConfirmados = input("Ingrese casos confirmados actuales: ")
		if len(str(codigo)) == 5:
			codigoRegion = int(str(codigo)[0:2])
		elif len(str(codigo)) == 4:
			codigoRegion = int(str(codigo)[0])
		else:
			print("El codigo de comuna no cumple los requisitos. Inténtelo nuevamente.")
			return
		cursor.execute(
			"""
			SELECT ID_REGION FROM CASOS_POR_REGION WHERE ID_REGION = :1
			""", [codigoRegion]
			)
		existe = cursor.fetchone()
		if existe == None:
			print("El código de la comuna indica que se debe crear una nueva región.")
			nombreRegion = input("Ingrese el nombre de la región: ")
			cursor.execute(
				"""
				INSERT INTO CASOS_POR_COMUNA VALUES (:1, :2, :3, :4)
				""", [codigo, nombre, casosConfirmados, poblacion]
				)
			cursor.execute(
				"""
				INSERT INTO CASOS_POR_REGION VALUES (:1, :2, :3, :4, :5)
				""", [codigoRegion, codigo, nombreRegion, casosConfirmados, poblacion])
			print("Comuna y región creadas con éxito.")
		else:
			print("Pasando...")
			cursor.execute(
				"""
				INSERT INTO CASOS_POR_COMUNA VALUES (:1, :2, :3, :4)
				""", [codigo, nombre, casosConfirmados, poblacion]
				)
			print("Pasando...")
			cursor.execute(
				"""
				SELECT NOMBRE_REGION FROM CASOS_POR_REGION WHERE ID_REGION = :1
				""", [codigoRegion]
				)
			print("Pasando...")
			nombreRegion = cursor.fetchone()
			print(codigoRegion, codigo, nombreRegion, casosConfirmados, poblacion)
			cursor.execute(
				"""
				INSERT INTO CASOS_POR_REGION VALUES (:1, :2, :3, :4, :5)	
				""", [codigoRegion, codigo, nombreRegion[0], casosConfirmados, poblacion]
				)
			print("Comuna creada con éxito.")
	else:
		print("El código a utilizar ya está ocupado. Inténtelo nuevamente.")

def insertarCSV(cursor):
	csvComunas = open("CasosConfirmadosPorComuna.csv", "r", encoding='utf-8')
	csvComunas = csv.reader(csvComunas)
	next(csvComunas)
	for linea in csvComunas:
		comuna = linea[0]
		codigoComuna = int(linea[1])
		poblacion = int(linea[2])
		casosConfirmados = int(linea[3])
		cursor.execute(
			"""
			INSERT INTO CASOS_POR_COMUNA VALUES (:1, :2, :3, :4)
			""", [codigoComuna, comuna, casosConfirmados, poblacion]
			)
	print("Inserción finalizada.")

def verCasos(cursor):
	codigoComuna = input("Ingrese el código de la comuna que desea ver: ")
	cursor.execute(
		"""
		SELECT ID_COMUNA FROM CASOS_POR_COMUNA WHERE ID_COMUNA = :1
		""", [codigoComuna]
		)
	existe = cursor.fetchone()
	if existe == None:
		print("La comuna que buscas no existe. Inténtalo nuevamente.")
	else:
		cursor.execute(
			"""
			SELECT NOMBRE_COMUNA, CASOS_CONFIRMADOS FROM CASOS_POR_COMUNA WHERE ID_COMUNA = :1
			""", [codigoComuna]
			)
		datos = cursor.fetchone()
		print("COMUNA 		CASOS CONFIRMADOS")
		print(datos[0] + "		" + str(datos[1]))

def verTodos(cursor):
	cursor.execute(
		"""
		SELECT NOMBRE_COMUNA, CASOS_CONFIRMADOS FROM CASOS_POR_COMUNA
		"""
		)
	datos = cursor.fetchall()
	if datos != None:
		print("COMUNA CASOS CONFIRMADOS")
		for comuna in datos:
			print(comuna[0] + "	" + str(comuna[1]))
	else:
		print("No existen comunas para mostrar.")