from Abstract.abstract import *
from math import *

class Trigonometricas(Expression):
    
    def __init__(self, left, tipo, fila, colum):
        self.left = left
        self.type = tipo
        super().__init__(fila, colum)
    
    def compilar(self, tree, table):
        if self.left != None:
            leftValue = self.left.compilar(tree, table)
        if self.type.compilar(None,None) == 'Seno':
            return sin(leftValue)
        elif self.type.compilar(None,None) == 'Coseno':
            return cos(leftValue)
        elif self.type.compilar(None,None) == 'Tangente':
            return tan(leftValue)
    
    
    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.colum