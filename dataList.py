"""
File: datLista.py
Author: Davide Rolino
Class for list of data.
"""

class DList(object):
    def __init__(self, name, unit='user'):
        self._name = name
        self._unit = unit #defite the mesure unit of the list of data
        self._list = []

#methods to get class' parameters
    def get_Name(self):
        return self._name

    def get_Unit(self):
        return self._unit

    def get_List(self):
        return self._list

#print method for the list
    def Print(self):
        print(self._name, '\t\u03C3Err(', self._name, ')') 
        for i in range(len(self._list)):
            print(self._list[i]._value, '\t', self._list)
