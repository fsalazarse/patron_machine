from abc import ABC, abstractmethod #Librerias para definir clases  y metodos abstractos


class Transition_state(ABC):

    @abstractmethod
    def error_transition(self, machine):
        pass

    @abstractmethod
    def transition_to_init(self, machine):
        pass

    @abstractmethod
    def transition_to_save_credential(self, machine):
        pass

    @abstractmethod
    def transition_to_scrapping(self, machine):
        pass

    @abstractmethod
    def transition_to_charge(self, machine):
        pass

    @abstractmethod
    def transition_charge(self, machine):
        pass

    @abstractmethod
    def transition_to_finish(self, machine):
        pass

    
            