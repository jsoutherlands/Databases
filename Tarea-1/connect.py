import cx_Oracle


def iniciar():
#	Solución de error de Carpeta instantclient.
#	En caso de fallo, revisar la dirección donde está alojado!
	print("Conectando...")
	lib_dir = r"D:\instantclient-basic-windows.x64-19.11.0.0.0dbru\instantclient_19_11"
	try:
		cx_Oracle.init_oracle_client(lib_dir=lib_dir)
	except:
		print("Error de conexión: cx_Oracle.init_oracle_client()")
		print(err);
		sys.exit(1);
	print("Conectando a la Base de Datos...")
	connection = cx_Oracle.connect("admin","admin","localhost:1521")
	print("Database Version: ", connection.version)
	cursor = connection.cursor()
	print("Conexión establecida.")
	return cursor,connection

def terminar(connection):
	connection.commit()
	connection.close()
	print("Conexión finalizada.")
