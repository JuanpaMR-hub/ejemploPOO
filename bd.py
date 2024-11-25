import oracledb
import getpass


#CREDENCIALES
user = 'SQLUSER'
pswd = getpass.getpass("Ingrese contraseña: ")
dsn = 'localhost/xe'


def hacer_consulta(query, tipo_query):
    try:
        #Crear conexion
        connection = oracledb.connect(user=user, password=pswd, dsn=dsn)
        
        # Crear cursor
        cursor = connection.cursor()
        
        try:
            if tipo_query == 'select':
                cursor.execute(query)
                return cursor.fetchall()
            else:
                cursor.execute(query)
                connection.commit()
        
        except Exception as e:
            print(f"Error al ejecutar query: {e}")
            connection.rollback()
        
        finally:
            # Cerrar cursor y conexion
            cursor.close()
            connection.close()
    
    except Exception as e:
        print(f"Hubo un error al intentar conectar a la base de datos: {e}")