from Abstract.abstract import *

class Primitivos(Expression):

    def __init__(self, value, tipo, line, column):
        self.value = value
        self.tipo = tipo
        self.tipoAux = ''
        super.__init__(self, line, column)
    
    def compilar(self, tree, table):
        return self.value
    
    def getTipo(self):
        return self.tipo