"""
File: data.py
Author: Davide Rolino
Last modified: 13/04/19
Class for a Physical data with: value, error
    for the moment the class will only work with maximum errors (not 3 sigma errors), also the formula for the propagation of the errors will be the ones approximate and not the one that involves the derivatives
"""

class Data(object):

    def __init__(self, value, error):
        self._value = value
        self._error = error

#methods to get class' parameters
    def getValue(self):
        return self._value

    def getError(self):
        return self._error
    
    #methods that work on class' parameters
    def getRelError(self):
        return self._error/self._value

    #override of standard methods
    def __str__(self): #print method
        result = str(self._value) + " " + u"\u00B1" + " " + str(self._error)
        return result

    def __add__(self, other): #override of add method
        newValue = self._value + other._value
        newError= self._error + other._error
        return Data(newValue, newError)

    def __sub__(self, other):
        newValue = self._value - other._value
        newError= self._error + other._error
        return Data(newValue, newError)

    def __mul__(self, other):
        newValue = self._value * other._value
        newError = newValue * (self.getRelError() + other.getRelError())
        return Data(newValue, newError)
    
    def __mul__(self, int):
        newValue = self._value
        newError = self._error
        return Data(newValue, newError)


    def __truediv__(self, other):
        newValue = self._value / other._value
        newError = newValue * (self.getRelError() + other.getRelError())
        return Data(newValue, newError)
