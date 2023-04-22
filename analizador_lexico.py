from Instrucciones.aritmeticas import Aritmeticas
from Instrucciones.tokens import *
from Abstract.tipo import Operacion
from Instrucciones.trigonometricas import Trigonometricas

reserved = {
    'ROPERACION'        :   'Operacion',
    'RVALOR1'           :   'Valor1',
    'RVALOR2'           :   'Valor2',
    'RSUMA'             :   'Suma',
    'RRESTA'            :   'Resta',
    'RMULTIPLICACION'   :   'Multiplicacion',
    'RDIVISION'         :   'Division',
    'RPOTENCIA'         :   'Potencia',
    'RRAIZ'             :   'Raiz',
    'RINVERSO'          :   'Inverso',
    'RSENO'             :   'Seno',
    'RCOSENO'           :   'Coseno',
    'RTANGENTE'         :   'Tangente',
    'RMODULO'           :   'Modulo',
    'RTEXTO'            :   'Texto',
    'RCOLORFONDONODO'   :   'Color-Fondo-Nodo',
    'RCOLORFUENTENODO'  :   'Color-Fuente-Nodo',
    'RFORMANODO'        :   'Forma-Nodo',
    'COMA'              :   ',',
    'PUNTO'             :   '.',
    'DPUNTOS'           :   ':',
    'CORI'              :   '[',
    'CORD'              :   ']',
    'LLI'               :   '{',
    'LLD'               :   '}',
}

tokens = list(reserved.values())
global n_linea
global n_columna
global instrucciones
global lista_tokens

n_linea = 1
n_columna = 1

errores = []
instrucciones = []
lista_tokens = []

def instruccion(cadena):
    global n_linea
    global n_columna
    global lista_tokens
    token = ''
    puntero = 0

    while cadena:
        char = cadena[puntero]
        puntero += 1
        if char == '\"':
            token, cadena = armar_token(cadena[puntero:])
            if token and cadena:
                n_columna += 1
                t = Token(token, n_linea, n_columna)
                lista_tokens.append(t)
                n_columna += len(token) + 1
                puntero = 0
        elif char.isdigit():
            token, cadena = armar_numero(cadena)
            if token and cadena:
                n_columna += 1
                t = Token(token, n_linea, n_columna)
                lista_tokens.append(t)
                n_columna += len(str(token)) + 1
                puntero = 0
        elif char == '[' or char == ']':
            t = Token(char, n_linea, n_columna)
            lista_tokens.append(t)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
        elif char == '\t':
            cadena = cadena[4:]
            puntero = 0
            n_columna += 4
        elif char == '\n':
            cadena = cadena[1:]
            puntero = 0
            n_linea += 1
            n_columna = 1
        else:
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1
    
def armar_token(cadena):
    token = ''
    puntero = ''  
    for char in cadena:
        puntero += char
        if char == '\"':
            return token, cadena[len(puntero):]
        else:
            token += char
    return None, None

# Aqui debo de armar el numero pero puede ser decimal asi como entero
def armar_numero(cadena):
    token = ''
    puntero = ''
    is_Decimal = False
    for char in cadena:
        puntero += char
        if char == '.':
            is_Decimal = True
        if char == '"' or char == ' ' or char == '\n' or char == '\t':
            if is_Decimal:
                return float(token), cadena[len(puntero)-1:]
            else:
                return int(token), cadena[len(puntero)-1:]
        else:
            token += char
    return None, None


# Aqui se crean las instrucciones
def ejecutar():
    global instrucciones
    global lista_tokens
    operacion = ''
    n1 = ''
    n2 = ''
    while lista_tokens:
        token = lista_tokens.pop(0)
        if token.getToken() == 'Texto':
            return None
        if token.getToken() == 'Operacion':
            operacion = lista_tokens.pop(0)
        elif token.getToken() == 'Valor1':
            n1 = lista_tokens.pop(0)
            if n1.getToken() == '[':
                n1 = ejecutar()
        elif token.getToken() == 'Valor2':
            n2 = lista_tokens.pop(0)
            if n2.getToken() == '[':
                n2 = ejecutar()
        
        if operacion and n1 and n2:
            return (Aritmeticas(n1, n2, operacion,f'Inicio: {operacion.getFila()} : {operacion.getColumna()}', f'Fin: {n2.getFila()} : {n2.getColumna()}'))
        
        if operacion and operacion.getToken() == ('Seno' or 'Coseno' or 'Tangente') and n1:
            return (Trigonometricas(n1, operacion,f'Inicio: {operacion.getFila()} : {operacion.getColumna()}', f'Fin: {n1.getFila()} : {n1.getColumna()}'))
    return None

def ejecutar_():
    global instrucciones
    while True:
        operacion = ejecutar()
        if operacion:
            instrucciones.append(operacion)
        else:
            break
    
    for instruccion in instrucciones:
        print(instruccion.compilar(None, None))



entrada = '''{
    {
        "Operacion":"Resta"
        "Valor1":6.5
        "Valor2":3.5
    },
    {
        "Operacion":"Multiplicacion"
        "Valor1":4
        "Valor2": [
            "Operacion":"Potencia"
            "Valor1":2
            "Valor2":[
                "Operacion":"Raiz"
                "Valor1":9
                "Valor2":2
                ]
        ]
    },
    {
        "Operacion":"Suma"
        "Valor1":[
        "Operacion":"Seno"
        "Valor1":90
        ]
        "Valor2":5.32
    }
    "Texto":"Realizacion de Operaciones"
    "Color-Fondo-Nodo":"Amarillo"
    "Color-Fuente-Nodo":"Rojo"
    "Forma-Nodo":"Circulo"
}'''

instruccion(entrada)
ejecutar_()