import csv
from tabulate import tabulate

def crearTabla(cursor):
	print("Creando Tabla Comunas...")
	cursor.execute(
		"""
			CREATE TABLE CASOS_POR_COMUNA(
			ID_REGION INTEGER NOT NULL,
			ID_COMUNA INTEGER NOT NULL,
			NOMBRE_COMUNA VARCHAR2(50) NOT NULL,
			CASOS_CONFIRMADOS INTEGER NOT NULL,
			POBLACION INTEGER NOT NULL,
			CONSTRAINT PK_COMUNA PRIMARY KEY (ID_COMUNA),
			CONSTRAINT FK_COMUNA FOREIGN KEY (ID_REGION) REFERENCES CASOS_POR_REGION(ID_REGION) ON DELETE CASCADE
			)
		"""
		)
	print("Tabla Regiones creada.")

def aumentarCasos(cursor):
	codigoComuna = int(input("Ingrese el código de la comuna: "))
	nuevos = int(input("Ingrese casos nuevos: "))
	if len(str(codigoComuna)) == 5:
		codigoRegion = int(str(codigoComuna)[0:2])
	elif len(str(codigoComuna)) == 4:
		codigoRegion = int(str(codigoComuna)[0])
	try:
		cursor.execute(
			"""
				SELECT * FROM CASOS_POR_COMUNA WHERE ID_COMUNA = :1 
			""", [codigoComuna])
		select = cursor.fetchone()
		var = select[0]
	except Exception as err:
		print("¡Error! La comuna no existe. Inténtalo de nuevo.")
	else:
		print("Actualizando tabla de comunas...")
		cursor.execute(
			"""
				UPDATE CASOS_POR_COMUNA
				SET CASOS_CONFIRMADOS = CASOS_CONFIRMADOS + :1
				WHERE ID_COMUNA = :2
			""", [nuevos, codigoComuna]
			)
		print("Actualizando tabla de regiones...")
		cursor.execute(
			"""
				UPDATE CASOS_POR_REGION
				SET CASOS_CONFIRMADOS = CASOS_CONFIRMADOS + :1
				WHERE ID_REGION = :2
			""", [nuevos, codigoRegion]
			)
		print("Agregación de casos nuevos exitosa.")
	finally:
		print("Operación finalizada...")

def disminuirCasos(cursor):
	codigoComuna = int(input("Ingrese el código de la comuna: "))
	nuevos = int(input("Ingrese casos a eliminar: "))
	if len(str(codigoComuna)) == 5:
		codigoRegion = int(str(codigoComuna)[0:2])
	elif len(str(codigoComuna)) == 4:
		codigoRegion = int(str(codigoComuna)[0])
	try:
		cursor.execute(
			"""
				SELECT * FROM CASOS_POR_COMUNA WHERE ID_COMUNA = :1 
			""", [codigoComuna])
		select = cursor.fetchone()
		var = select[0]
	except Exception as err:
		print("¡Error! La comuna no existe. Inténtalo de nuevo.")
	else:
		print("Actualizando tabla de comunas...")
		cursor.execute(
			"""
				UPDATE CASOS_POR_COMUNA
				SET CASOS_CONFIRMADOS = CASOS_CONFIRMADOS - :1
				WHERE ID_COMUNA = :2
			""", [nuevos, codigoComuna]
			)
		print("Actualizando tabla de regiones...")
		cursor.execute(
			"""
				UPDATE CASOS_POR_REGION
				SET CASOS_CONFIRMADOS = CASOS_CONFIRMADOS - :1
				WHERE ID_REGION = :2
			""", [nuevos, codigoRegion]
			)
		print("Disminución de casos nuevos exitosa.")
	finally:
		print("Operación finalizada...")

def crearComuna(cursor):
	codigo = input("Ingrese codigo de comuna\n(DEBE tener entre 4 y 5 números. Si tiene 4, el primer dígito es el código de la región. Si tiene 5, los dos primeros dígitos son el código de la región): ")
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
		if cursor == None:
			print("El código de la comuna indica que se debe crear una nueva región.")
			nombreRegion = input("Ingrese el nombre de la región a crear: ")
			cursor.execute(
				"""
				INSERT INTO CASOS_POR_REGION VALUES (:1, :2, :3, :4)
				""", [codigoRegion, nombreRegion, casosConfirmados, poblacion]
				)
			cursor.execute(
				"""
				INSERT INTO CASOS_POR_COMUNA VALUES (:1, :2, :3, :4, :5)
				""", [codigoRegion, codigo, nombre, casosConfirmados, poblacion]
				)
			print("Comuna y región creadas con éxito.")
		else: #Existe la región, solo sumar casos a region
			cursor.execute(
				"""
				INSERT INTO CASOS_POR_COMUNA VALUES (:1, :2, :3, :4, :5)
				""", [codigoRegion, codigo, nombre, casosConfirmados, poblacion]
				)
			cursor.execute(
				"""
				UPDATE CASOS_POR_REGION
				SET CASOS_CONFIRMADOS = CASOS_CONFIRMADOS + :1,
				SET POBLACION = POBLACION + :2
				WHERE ID_REGION = :3
				""", [casosConfirmados, poblacion, codigoRegion]
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
		if len(str(codigoComuna)) == 5:
			codigoRegion = int(str(codigoComuna)[0:2])
		elif len(str(codigoComuna)) == 4:
			codigoRegion = int(str(codigoComuna)[0])
		cursor.execute(
			"""
			INSERT INTO CASOS_POR_COMUNA VALUES (:1, :2, :3, :4, :5)
			""", [codigoRegion, codigoComuna, comuna, casosConfirmados, poblacion]
			)
		cursor.execute(
			"""
			UPDATE CASOS_POR_REGION
			SET CASOS_CONFIRMADOS = CASOS_CONFIRMADOS + :1,
				POBLACION = POBLACION + :2
			WHERE ID_REGION = :3
			""", [casosConfirmados, poblacion, codigoRegion]
			)
	print("Inserción finalizada.")

def verCasos(cursor):
	codigoComuna = input("Ingrese el código de la comuna que desea ver: ")
	try:
		cursor.execute(
			"""
			SELECT NOMBRE_COMUNA, CASOS_CONFIRMADOS FROM CASOS_POR_COMUNA WHERE ID_COMUNA = :1
			""", [codigoComuna])
		datos = cursor.fetchall()
		var = datos[0][0]
	except Exception as err:
		print("¡Error! La comuna no existe. Inténtalo de nuevo.")
	else:
		print(tabulate(datos, ['COMUNA', "CASOS CONFIRMADOS"], tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))
	finally:
		print("Operación finalizada...")

def verTodos(cursor):
	try:
		cursor.execute(
		"""
		SELECT NOMBRE_COMUNA, CASOS_CONFIRMADOS FROM CASOS_POR_COMUNA
		"""
		)
		datos = cursor.fetchall()
		var = datos[0][0]
	except Exception as err:
		print("No existen comunas para mostrar.")
	else:
		print(tabulate(datos, ['COMUNAS', "CASOS CONFIRMADOS"], tablefmt='fancy_grid', stralign='center', floatfmt='.0f'))
	finally:
		print("Operación finalizada...")

def top5Comunas(cursor):
	try:
		cursor.execute(
			"""
				SELECT NOMBRE_COMUNA, ROUND(((CASOS_CONFIRMADOS/POBLACION)*100),2) AS POSITIVIDAD_COMUNAL FROM CASOS_POR_COMUNA ORDER BY POSITIVIDAD_COMUNAL DESC
			""")
		datos = cursor.fetchmany(5)
		var = datos[0][0]
	except Exception as err:
		print("No es posible mostrar el top 5 dado que no existen comunas.")
	else:
		print(tabulate(datos, ["COMUNA","POSITIVIDAD COMUNAL [%]"], tablefmt='fancy_grid', stralign='center'))

def combinarComunas(cursor):
	comuna1 = int(input("Ingrese el código de la comuna a combinar: "))
	comuna2 = int(input("Ingrese el código de la otra comuna a combinar: "))
	nombreComuna = input("Ingrese el nombre de la comuna combinada: ")
	row = []
	cursor.execute(
		"""
			SELECT * FROM CASOS_POR_COMUNA WHERE ID_COMUNA = :1
		""",[comuna1]
		)
	row.append(cursor.fetchone())
	cursor.execute(
		"""
			SELECT * FROM CASOS_POR_COMUNA WHERE ID_COMUNA = :1
		""",[comuna2]
		)
	row.append(cursor.fetchone())
	if len(row) != 2:
		print("Error: Una o ambas comunas no existen. Inténtalo nuevamente.")
		print("Operación finalizada...")
		return
	if row[0][0] != row[1][0]:
		print("Las comunas pertenecen a regiones distintas.")
		codigoRegion = int(input("Ingrese una de las siguientes opciones:\n 1 | Pertenecer a la región {}.\n 2 | Pertenecer a la región {}.\n Opción: ".format(row[0][0],row[1][0])))
		if codigoRegion == 1:
			codigoRegion = row[0][0]
			oldRegion = row[1][0]
			casosConfirmados = row[1][3]
			poblacion = row[1][4]
			codigoComuna = comuna1
			oldComuna = comuna2
		elif codigoRegion == 2:
			codigoRegion = row[1][0]
			oldRegion = row[0][0]
			casosConfirmados = row[0][3]
			poblacion = row[0][4]
			codigoComuna = comuna2
			oldComuna = comuna1
		else:
			print("Opción no válida.")
			print("Operación finalizada...")
			return
		cursor.execute(
			"""
				UPDATE CASOS_POR_REGION
				SET CASOS_CONFIRMADOS = CASOS_CONFIRMADOS - :1,
					POBLACION = POBLACION - :2
				WHERE ID_REGION = :3
			""", [casosConfirmados, poblacion, oldRegion]
			)
		cursor.execute(
			"""
				UPDATE CASOS_POR_REGION
				SET CASOS_CONFIRMADOS = CASOS_CONFIRMADOS + :1,
					POBLACION = POBLACION + :2
				WHERE ID_REGION = :3
			""", [casosConfirmados, poblacion, codigoRegion]
			)
	else:
		casosConfirmados = row[1][3]
		poblacion = row[1][4]
		codigoComuna = comuna1
		oldComuna = comuna2
	cursor.execute(
		"""
			UPDATE CASOS_POR_COMUNA
			SET NOMBRE_COMUNA = :1,
				CASOS_CONFIRMADOS = CASOS_CONFIRMADOS + :2,
				POBLACION = POBLACION + :3
			WHERE ID_COMUNA = :4
		""", [nombreComuna, casosConfirmados, poblacion, codigoComuna]
		)
	cursor.execute(
		"""
			DELETE FROM CASOS_POR_COMUNA
			WHERE ID_COMUNA = :1
		""", [oldComuna]
		)
	print("Combinación de comunas realizada con éxito.")
