"""
File: datLista.py
Author: Davide Rolino
Class for sets of data. The aim of a DSet is to store all the DList regarding one measurement. 
All the DList must be the same lenght or the function newData will return an error
"""

class DSet(object):
    def __init__(self, name, lenght):
        self._name = name
        self._lenght = lenght
        self._set = {}

#methods to get class' parameters
    def get_Name(self):
        return self._name

    def get_List(self):
        return self._set