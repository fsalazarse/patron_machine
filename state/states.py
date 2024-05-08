
from interface.interface import Transition_state
from  connection_db.querys import Querys
import time
import requests

class Init_state(Transition_state):

    def transition_to(self, machine):
        print("--------------------------------------------------------------")
        print(" 1. Estado init:  Machine a comenzado el Trabajo")
        print("--------------------------------------------------------------")
        machine.state = Save_credentials()


class Save_credentials(Transition_state):
    """ Obtenemos la registros de la la nube y los guardamos en la base de datos"""
    def transition_to(self, machine):
        querys = Querys()
        querys.insert_data(rut="19209998-6", password="ff33", status="not_process")
        time.sleep(2)
        querys.insert_data(rut="16209996-6", password="ff33", status="not_process")
        time.sleep(2)
        querys.insert_data(rut="15209962-6", password="ff33", status="not_process")
        
        print("--------------------------------------------------------------")
        print(" 2. Estado Save_credentials:  Machine A obtenido los datos desde la nube y los a guardado en sqlite3")
        print("--------------------------------------------------------------")

        machine.state = Scrapping()


class Scrapping(Transition_state):

    def populate_srapping_table(self, creds):
        """poblar table de scrapping con datos falsos para laboratorio"""
        try:
            ruts = [cred[1] for cred in creds]
            querys = Querys()
            querys.insert_data_scrapping(ruts[0], 12, 33)
            querys.insert_data_scrapping(ruts[1], 44, 78)
            querys.insert_data_scrapping(ruts[2], 12, 99)
                
        except Exception as error:
            raise error

    def transition_to(self, machine):
        """Function heredada de la funcion abstracta"""
        try:
            querys = Querys()
            creds = querys.get_creds()
            self.populate_srapping_table(creds=creds)

            print("--------------------------------------------------------------")
            print(" 3. Estado Scrapping:  Machine ha registrado los datos en la tabla de scrapping")
            print("--------------------------------------------------------------")

        except Exception as error:
            print("Scrapping()", error)
        ##return super().transition_to(machine)

        machine.state = To_charge()


class To_charge(Transition_state):

    def clear_data(self):
        try:
            querys = Querys()
            rows = querys.get_data_scrapping()
            clear_data = [tuple(item for item in row if item is not None) for row in rows]
            return clear_data
        except Exception as error:
            raise error

    def transition_to(self, machine):
        data = self.clear_data()
        querys = Querys()
        for row in data:
            querys.insert_data_to_chart(row)
        
        print("--------------------------------------------------------------")
        print(" 4. Estado To_charge: Datos preparados y listos para ser subidos a firestore")
        print("--------------------------------------------------------------")
        machine.state = Charge()


class Charge(Transition_state):
     
     def verificar_conexion_internet(self):
        try:
            # Intenta hacer una solicitud a una página web, por ejemplo, google.com
            response = requests.get("http://www.google.com", timeout=5)
            # Si la solicitud fue exitosa (código de estado 200), devuelve True
            return response.status_code == 200
        except requests.ConnectionError:
            # Si hay un error de conexión, devuelve False
            return False

     def transition_to(self, machine):
        try:
        
            exist_conextion = self.verificar_conexion_internet()
            print("--------------------------------------------------------------")
            print(" 5. Estado Charge: cambio a estado charge")
            if exist_conextion:
                
                print(" 5. Estado Charge: Datos subidos a firestore")
                print("--------------------------------------------------------------")
                machine.state = Finish()
            else:
                raise ValueError("No fue posible realizar una conexion a internet!!!!!!")
        except Exception as error:
           # machine.state = Aborted()
            print(" Error in charge", error)


class Finish(Transition_state):
    def transition_to(self, machine):
        try:
            print("--------------------------------------------------------------")
            print(" 6. Estado Finish: Trabajo finalizado")
            print("--------------------------------------------------------------")
        except Exception as error:
            print(" Error in Finish()", error)


# class Aborted(Transition_state):
    
#     def transition_to(self, machine):
#             try:
#                 print("--------------------------------------------------------------")
#                 print(" 6. Estado Aborted: Se presento un error al intentar seguir con el proceso")
#                 print("--------------------------------------------------------------")
#             except Exception as error:
#                 print("Error in aborted", error)