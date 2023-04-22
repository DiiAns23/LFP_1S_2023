
class Aritmeticas:

    pi = 3.1416 # Atributo de clase

    def __init__(self, valor1, valor2):
        self.a = valor1
        self.b = valor2

    def getA(self):
        return self.a

    def setA(self, valor):
        self.a = valor

    def suma(self):
        return self.a + self.b

    def resta(self):
        return self.a - self.b

    def multiplicacion(self):
        return self.a * self.b

    def division(self):
        # Si b es 0, no se puede dividir
        if self.b == 0:
            return None
        return self.a / self.b
    
    def getPi(self):
        return self.pi
    
    def setPi(self, valor):
        self.pi = valor


# Declaramos una instancia de la clase Aritmeticas

operacion = Aritmeticas(10, 5)

# Imprimimos los resultados de las operacion suma
print(operacion.suma())

# Imprimimos los resultados de las operacion resta
print(operacion.resta())

# Imprimimos los resultados de las operacion multiplicacion
print(operacion.multiplicacion())

# Imprimimos los resultados de las operacion division
print(operacion.division())

# Imprimimos el valor de a
print('Mandado a traer como funcion',operacion.getA())
print('Mandado a traer como variable o atributo de clase',operacion.a)

# Cambiamos el valor de a
operacion.setA(20)

# Imprimimos el valor de a
print('Mandado a traer como funcion',operacion.getA())

# Imprimimos los resultados de las operacion suma
print(operacion.suma())

# Imprimir Pi
print(operacion.getPi())

# Cambiar el valor de Pi
operacion.setPi(3.14)

# Imprimir Pi
print(operacion.getPi())

# Declaramos otra instancia de la clase Aritmeticas
operacion_2 = Aritmeticas(20, 10)
print(operacion_2.getPi())