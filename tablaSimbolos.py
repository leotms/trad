#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
Creado el 22/02/2015
Ult. Modificacion el 22/02/2015

@author:  Aldrix Marfil     10-10940
@author:  Leonardo Martinez 11-10576
'''

class Table:

    def getIdent(self,level):
        return level * 4

    def printValueIdented(self, value, level):
        print self.getIdent(level)* " " + str(value)


class Simbolo(Table):

    def __init__(self, name, dataType, value = None):
        self.name = name
        self.type = dataType
        self.value = value

    def printTable(self, level):
        if self.value:
            valor = "| Value: " + str(self.value)
        else:
            valor = ""

        string  = "Variable: " + str(self.name) 
        string += " | Type: " + str(self.type)
        string += valor
        self.printValueIdented(string, level)

class tablaSimbolos(Table):

    def __init__(self):
        self.scope  = {}
        self.outer  = None
        self.errors = []

    def printTable(self, level):
        self.printValueIdented("SCOPE\n",level)
        for symbol in self.scope:
            self.scope[symbol].printTable(level + 1)
        self.printValueIdented("END_SCOPE\n",level)
        if self.outer:
            self.outer.printTable(level + 1)


    def insert(self, variable, dataType):
        if not self.contains(variable):
            self.scope[variable] = Simbolo(variable, dataType)
        else:
            string = "Variable " + str(variable) + " already in scope"
            self.error(string)

    def delete(self, variable):
        if self.contains(variable):
            del self.scope[variable]
        else:
            string ="No '" + variable+ "' in scope"
            self.error(string)

    def update(self, variable, dataType, value):
        if self.contains(variable):
            if variable in self.scope:
                symbol = self.scope[variable]

                if dataType == symbol.dataType:
                    symbol.value = value
                    self.scope[variable] = symbol
                    return True
                else:
                    string = "SymTable.update: Different data types"
                    self.error.append(string)
                    return False
            else:
                return self.outer.update(variable, dataType, value)
        else:
            print "SymTable.update: No " + variable + " in scope"
            return False

    def contains(self, variable):
        if self.scope:
            print(str(self.scope))
            if variable in self.scope:
                return True
        else:
            return False

    def lookup(self, value):
        pass


    def error(self, mensaje):
        self.errors.append(mensaje)
