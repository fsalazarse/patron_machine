from dataclasses import dataclass
from states import Init_state

@dataclass
class Machine: 

    """
        El Contexto define la interfaz de interés para los clientes. También mantiene
        una referencia a una instancia de una subclase de Estado, que representa la situación actual
        estado del contexto.
    """

    state = Init_state() #Una referencia al estado actual del contexto.

    def updateState(self):
        self.state.transition_to(self)
    
