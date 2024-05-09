
from interface.interface import Transition_state
from  connection_db.querys import Querys
import time
import requests

class Init_state(Transition_state):

    def error_transition(self, machine):
        querys = Querys()
        querys.update_status_message("Aborted")
        machine.state = Aborted()

    def transition_to_init(self, machine):
        pass

    def transition_to_save_credential(self, machine):
        print("--------------------------------------------------------------")
        print(" 1. Estado init:  Machine a comenzado el Trabajo")
        print("--------------------------------------------------------------")
        machine.state = Save_credentials()

    def transition_to_scrapping(self, machine):
        pass

    def transition_to_charge(self, machine):
        pass

    def transition_charge(self, machine):
        pass

    def transition_to_finish(self, machine):
        pass

class Save_credentials(Transition_state):
    """ Obtenemos la registros de la la nube y los guardamos en la base de datos"""

    def error_transition(self, machine):
        print("error en el proceso interno del estado")

    def transition_to_init(self, machine):
        pass

    def transition_to_save_credential(self, machine):
        pass

    def transition_to_scrapping(self, machine):
        querys = Querys()
        querys.insert_data(rut="19209998-6", password="ff33", status="not_process")
        time.sleep(2)
        querys.insert_data(rut="16209996-6", password="ff33", status="not_process")
        time.sleep(2)
        querys.insert_data(rut="15209962-6", password="ff33", status="not_process")
        
        print("--------------------------------------------------------------")
        print(" 2. Estado Save_credentials:  Machine A obtenido los datos desde la nube y los a guardado en sqlite3")
        print("--------------------------------------------------------------")

        querys.update_status_message("save_credential")
        machine.state = Scrapping()

    def transition_to_charge(self, machine):
        pass

    def transition_charge(self, machine):
        pass

    def transition_to_finish(self, machine):
        pass
   
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

    def error_transition(self, machine):
        print("error en el proceso interno del estado")

    def transition_to_init(self, machine):
        pass

    def transition_to_save_credential(self, machine):
        pass

    def transition_to_scrapping(self, machine):
        pass

    def transition_to_charge(self, machine):
        """Function heredada de la funcion abstracta"""
        try:
            querys = Querys()
            creds = querys.get_creds()
            self.populate_srapping_table(creds=creds)

            print("--------------------------------------------------------------")
            print(" 3. Estado Scrapping:  Machine ha registrado los datos en la tabla de scrapping")
            print("--------------------------------------------------------------")
            querys.update_status_message("scrapping")
            machine.state = To_charge()
        except Exception as error:
            print("Scrapping()", error)
  
    def transition_charge(self, machine):
        pass

    def transition_to_finish(self, machine):
        pass

class To_charge(Transition_state):

    def clear_data(self):
        try:
            querys = Querys()
            rows = querys.get_data_scrapping()
            clear_data = [tuple(item for item in row if item is not None) for row in rows]
            return clear_data
        except Exception as error:
            raise error

    def error_transition(self, machine):
        print("error en el proceso interno del estado")

    def transition_to_init(self, machine):
        pass

    def transition_to_save_credential(self, machine):
        pass

    def transition_to_scrapping(self, machine):
        """Function heredada de la funcion abstracta"""
        pass

    def transition_to_charge(self, machine):
        pass

    def transition_charge(self, machine):
        data = self.clear_data()
        querys = Querys()
        for row in data:
            querys.insert_data_to_chart(row)
        
        print("--------------------------------------------------------------")
        print(" 4. Estado To_charge: Datos preparados y listos para ser subidos a firestore")
        print("--------------------------------------------------------------")
        querys.update_status_message("to_charge")
        machine.state = Charge()

    def transition_to_finish(self, machine):
        pass

class Charge(Transition_state):
     
    def error_transition(self, machine):
        print("error en el proceso interno del estado")

    def transition_to_init(self, machine):
        pass

    def transition_to_save_credential(self, machine):
        pass

    def transition_to_scrapping(self, machine):
        """Function heredada de la funcion abstracta"""
        pass

    def transition_to_charge(self, machine):
        pass

    def transition_charge(self, machine):
        pass

    def transition_to_finish(self, machine):
        try:
            querys = Querys()
            exist_conextion = input("Simular error?: ")
            print("--------------------------------------------------------------")
            print(" 5. Estado Charge: cambio a estado charge")
            
            if exist_conextion == "no":
                
                print(" 5. Estado Charge: Datos subidos a firestore")
                querys.update_status_message("finish")
                print(" 5. Estado Charge: Datos  estado cambiado a finish")
                print("--------------------------------------------------------------")
                machine.state = Finish()
            else:
                raise ValueError("No fue posible realizar una conexion a internet!!!!!!")
        except Exception as error:
           # machine.state = Aborted()
            querys.update_status_message("error")
            print(" Error in charge", error)

class Finish(Transition_state):
   
    def error_transition(self, machine):
        print("error en el proceso interno del estado")

    def transition_to_init(self, machine):
        pass

    def transition_to_save_credential(self, machine):
        pass

    def transition_to_scrapping(self, machine):
        """Function heredada de la funcion abstracta"""
        pass

    def transition_to_charge(self, machine):
        pass

    def transition_charge(self, machine):
        pass

    def transition_charge(self, machine):
        pass

    def transition_to_finish(self, machine):
        print("Fin del proceso")


class Aborted(Transition_state):
    
    def error_transition(self, machine):
        pass

    def transition_to_init(self, machine):
        pass

    def transition_to_save_credential(self, machine):
        pass

    def transition_to_scrapping(self, machine):
        """Function heredada de la funcion abstracta"""
        pass

    def transition_to_charge(self, machine):
        pass

    def transition_charge(self, machine):
        machine.state = Charge()


    def transition_to_finish(self, machine):
        pass
