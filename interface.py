from abc import ABC, abstractmethod #Librerias para definir clases  y metodos abstractos


class Transition_state(ABC):
    @abstractmethod
    def transition_to(self, machine): 
        pass
            