
from interface import Transition_state


class Init_state(Transition_state):

    def transition_to(self, machine):
        print("Machine actualizando estado a init")
        machine.state = Get_credentials()


class Get_credentials(Transition_state):

    def transition_to(self, machine):
         print("Machine actualizando estado a Get_credentials ")
