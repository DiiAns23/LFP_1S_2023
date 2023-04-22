from Abstract.abstract import *

class Token(Expression):
    
    def __init__(self, token, fila, colum):
        self.token = token
        super().__init__(fila, colum)
    
    def compilar(self, tree, table):
        return self.token
    
    def getToken(self):
        return str(self.token)
    
    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.colum