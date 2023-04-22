from abc import ABC, abstractmethod

class Expression(ABC):
    
    def __init__(self, fila, colum):
        self.fila = fila
        self.colum = colum
    
    @abstractmethod
    def compilar(self, tree, table):
        pass