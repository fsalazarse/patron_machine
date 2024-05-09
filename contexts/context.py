from dataclasses import dataclass
from state.states import Init_state

@dataclass
class Machine: 

    """
        El Contexto define la interfaz de interés para los clientes. También mantiene
        una referencia a una instancia de una subclase de Estado, que representa la situación actual
        estado del contexto.
    """

    state = Init_state() #Una referencia al estado actual del contexto.

    def updateError(self):
        self.state.error_transition(self)
   
    def update_to_init(self):
        self.state.transition_to_init(self)

    def update_to_save_credential(self):
        self.state.transition_to_save_credential(self)
   
    def update_to_scrapping(self):
        self.state.transition_to_scrapping(self)

    def update_to_charge(self):
        self.state.transition_to_charge(self)

    def update_charge(self):
        self.state.transition_charge(self)

    def update_to_finish(self):
        self.state.transition_to_finish(self)