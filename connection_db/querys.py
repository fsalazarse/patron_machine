from dataclasses import dataclass
from connection_db.conextion import Connection

@dataclass
class Querys:
    connection =  Connection().connection_sqlite3()

    def get_creds(self):
        try:
            """Obtener Mensaje a procesar con un estatus init"""
            cursor, conn = self.connection
            cursor.execute("SELECT * FROM creds")
            row = cursor.fetchall()
            return row
        except Exception as error:
            raise error


    def insert_data(self, rut, password, status):
        try: 
            """Obtener Mensaje a procesar con un estatus init"""
            cursor, conn = self.connection
            cursor.execute('INSERT INTO creds (rut, password, status) VALUES (?, ?, ?)', (rut, password, status))
            conn.commit()
           
        except Exception as error:
            raise error
        

    def insert_data_scrapping(self, rut, number_1, number_2):
        try: 
            """Obtener Mensaje a procesar con un estatus init"""
            cursor, conn = self.connection
            cursor.execute('INSERT INTO scrapping (rut, number_1, number_2) VALUES (?, ?, ?)', (rut, number_1, number_2))
            conn.commit()
           
        except Exception as error:
            raise error
      
    
    def get_data_scrapping(self):
        try:
            """Obtener los datos de la tabla de scrapping"""
            cursor, conn = self.connection
            cursor.execute("SELECT * FROM scrapping")
            rows = cursor.fetchall()
            return rows
        except Exception as error:
            raise error


    def insert_data_to_chart(self, row):
        try: 
            """Obtener Mensaje a procesar con un estatus init"""
            cursor, conn = self.connection
            cursor.execute('INSERT INTO to_chart (rut, number_1, number_2, number_3, Timestamp) VALUES (?, ?, ?, ? ,?)', row)
            conn.commit()
           
        except Exception as error:
            raise error
        
    
    def get_message(self):
        try:
            cursor, conn = self.connection
            cursor.execute("SELECT * FROM message")
            message = cursor.fetchall()
            return message[0]
            

        except Exception as error:
            print("get_message", error)

    def update_status_message(self, nuevo_valor):
        try:
           
            cursor, conn = self.connection
            consulta = """
                UPDATE message
                SET status = ?  -- Los valores a actualizar
                WHERE id = ?  -- La condición para seleccionar el registro a actualizar
            """
            # Valores para la actualización
            
            condicion = 1

            # Ejecutar la consulta
            cursor.execute(consulta, (nuevo_valor, condicion))
            # Confirmar los cambios
            conn.commit()

        except Exception as error:
            print("update_status_message()", error)

    def close_db(self):
        try:
            """Cerrar coneccion con la base de datos"""
            cursor, conn = self.connection
            conn.close()
        except Exception as error:
            raise error
