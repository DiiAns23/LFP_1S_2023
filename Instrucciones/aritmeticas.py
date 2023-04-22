from Abstract.abstract import *
from math import *

class Aritmeticas(Expression):
    
    def __init__(self, left, right, tipo, fila, colum):
        self.left = left
        self.right = right
        self.type = tipo
        super().__init__(fila, colum)
    
    def compilar(self, tree, table):
        if self.left != None:
            leftValue = self.left.compilar(tree, table)
            
        if self.right != None:
            rightValue = self.right.compilar(tree, table)

        if self.type.compilar(None,None) == 'Suma':
            return leftValue + rightValue
        elif self.type.compilar(None,None) == 'Resta':
            return leftValue - rightValue
        elif self.type.compilar(None,None) == 'Multiplicacion':
            return leftValue * rightValue
        elif self.type.compilar(None,None) == 'Division':
            return leftValue / rightValue
        elif self.type.compilar(None,None) == 'Potencia':
            return leftValue ** rightValue
        elif self.type.compilar(None,None) == 'Modulo':
            return leftValue % rightValue
        elif self.type.compilar(None,None) == 'Raiz':
            return leftValue ** (1/rightValue)
        elif self.type.compilar(None,None) == 'Inverso':
            return 1/leftValue
    
    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.colum
