from contexts.context import Machine

if __name__ =="__main__":

    """Simulo que ya tengo el mensaje con el que deceo trabajar"""
    status = "init"
    play = Machine() #Instancio maquina de estados
    if status == "init":
        #Inicia proceso de init
        play.updateState()
        #Inicia proceso de save credencials
        play.updateState()
        #Inicia proceso de scrapping
        play.updateState()
        #Inicia proceso de to_charge
        play.updateState()
        #Iniciar proceso de carga
        play.updateState()
        #Iniciar proceso de Finish     
        play.updateState()



    

