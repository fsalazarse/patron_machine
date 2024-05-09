from contexts.context import Machine
from connection_db.querys import Querys

if __name__ =="__main__":

    """Simulo que ya tengo el mensaje con el que deceo trabajar"""
    status = "init"
    play = Machine() #Instancio maquina de estados

    message = Querys().get_message()
    print(message)

    if message[2] == "init":

        try:
            #Inicia proceso de save credencials
            play.update_to_init()
            #Inicia proceso de save credencials
            play.update_to_save_credential()
            #Inicia proceso de scrapping
            play.update_to_scrapping()
            #Inicia proceso de to_charge
            play.update_to_charge()
            #Iniciar proceso de carga
            play.update_charge()

            play.update_to_finish()


        except Exception as err:
            pass





    elif message[2] == "error":
        play.updateError()
        play.update_charge()
        play.update_to_finish()

    else:

        pass

