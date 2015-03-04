#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Creado el 22/02/2015
Ult. Modificacion el 22/02/2015

@author:  Aldrix Marfil     10-10940
@author:  Leonardo Martinez 11-10576
'''


# Funciones para la impresion
# Devuelve la identacion adecuada al nivel
def getIdent(level):
    return level * 4

# Imprime en pantalla un valor identado
def printValueIdented(value, level):
    print getIdent(level)* " " + str(value)

# Clase Simbolo
class Simbolo(object):

    global symbol_default
    symbol_default = {
        'int' : 0,
        'bool': 'false',
        'set' : '{}'
    }

    def __init__(self, name, type, modifiable, value = None):
        self.name       = name
        self.type       = type
        self.modifiable = modifiable
        # Colocamos el valor por defecto
        if value == None:
            self.value = symbol_default[type]
        else:
            self.value = value

    def printTable(self, level):
        string  = "Variable: " + self.name
        string += " | Type: "   + self.type
        string += " | Value: " + str(self.value)
        string += " | Modifiable: " + str(self.modifiable)
        printValueIdented(string, level)

# Clase Tabla de Simbolos, provee lo necesario para construir una 
# nueva tabla de simbolos.
class tablaSimbolos(object):

    def __init__(self):
        self.symbols  = {}
        self.parent   = None
        self.children = []
        # Comentado en caso de ser utilizado mas adelante.
        # self.errors  = []

    # Imprime los simbolos de la tabla actual y de sus sucesoras.
    def printTable(self, level):
        
        # La tabla actual    
        if self.symbols != {}:
            printValueIdented("SCOPE",level)
            for symbol in self.symbols:
                self.symbols[symbol].printTable(level + 1)
            # Se imprimen los hijos
            if self.children:
                for child in self.children:
                    child.printTable(level + 1)
            printValueIdented("END_SCOPE",level)
        # Si la tabla solo tiene hijos, se imprimen
        elif self.children:
            for child in self.children:
                child.printTable(level)    
        # Si la tabla es vacia      
        else:
            printValueIdented("SCOPE",level)
            printValueIdented("END_SCOPE",level)

    # Comprueba si una variable esta delcarada en la tabla
    # de simbolos actual
    def contains(self, variable):
        if self.symbols:
            return (variable in self.symbols)
        return False

    # Comprueba si una variable esta declarada en la tabla de 
    # simbolos global
    def globalContains(self, variable):
        if self.symbols:
            return (variable in self.symbols)
        if self.parent:
            return self.parent.globalContains(variable)
        return False

    # Busca una variable de manera global declarada en la tabla 
    # de simbolos.
    def buscar(self, variable):
        if self.symbols:
            if variable in self.symbols:
                return self.symbols[variable]
            else:
                if self.parent:
                    return self.parent.buscar(variable)
        else:
            print "Variable " + str(variable) + " no esta definida."

    #Inserta un simbolo en la tabla de simbolos local
    def insert(self, variable, dataType, modifiable = True):
        if not self.contains(variable):
            self.symbols[variable] = Simbolo(variable, dataType, modifiable)
        else:
            string = "Variable '" + str(variable) + "' ya esta definida."
            print(string)
            #self.error(string)

    # Elimina un simbolo de la tabla de simbolos actual
    def delete(self, variable):
        if self.contains(variable):
            del self.symbols[variable]
        else:
            string = "Variable '" + variable+ "' no definida."
            self.error(string)

    # def update(self, variable, dataType, value):
    #     if self.contains(variable):
    #         if variable in self.symbols:
    #             symbol = self.symbols[variable]

    #             if dataType == symbol.dataType:
    #                 symbol.value = value
    #                 self.symbols[variable] = symbol
    #                 return True
    #             else:
    #                 string = "SymTable.update: Different data types"
    #                 self.error.append(string)
    #                 return False
    #         else:
    #             return self.outer.update(variable, dataType, value)
    #     else:
    #         print "SymTable.update: No " + variable + " in symbols"
    #         return False

    # def lookup(self, value):
    #     pass

    # def error(self, mensaje):
    #     self.errors.append(mensaje)
