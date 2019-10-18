"""
File: data.py
Author: Davide Rolino
Last modified: 10/04/19
Class for a Physical data with: value, error, unit of mesure (mks)
    for the moment the class will only work with maximum errors (not 3 sigma errors), also the formula for the propagation of the errors will be the ones approximate and not the one that involves the derivatives
"""

class Data(object):

    def __init__(self, value, error, unitUp, unitDown):
        self._value = value
        self._error = error
        self._unitUp  = unitUp
        self._unitDown = unitDown

  #methods to get class' parameters
    def getValue(self):
        return self._value

    def getError(self):
        return self._error

    def getUnitUp(self):
        return self._unitUp

    def getUnitDown(self):
        return self._unitDown
    
    #methods that work on class' parameters
    def getRelError(self):
        return self._error/self._value

    #override of standard methods
    def __str__(self): #print method
        result = str(self._value) + " " + u"\u00B1" + " " + str(self._error) + " " 
        if self._unitUp == " " and self._unitDown == " ":
            result +=  " "
        elif self._unitUp == " " and self._unitDown != " ":
            result +=  "1/" + str(self._unitDown)
        elif self._unitUp != " " and self._unitDown == " ":
            result += str(self.unitUp)
        else:
            result += str(self._unitUp) + "/" + str(self._unitDown)
        return result

    def __add__(self, other): #override of add method
        if self._unitUp == other._unitUp and self._unitDown == other._unitDown:
            newValue = self._value + other._value
            newError= self._error + other._error
            return Data(newValue, newError, self._unitUp, self._unitDown)
        else:
            print ("Errore stai sommando mele e banane")
            return Data(0, 0, " ", " ")

    def __sub__(self, other):
        if self._unitUp == other._unitUp and self._unitDown == other._unitDown:
            newValue = self._value - other._value
            newError= self._error + other._error
            return Data(newValue, newError, self._unitUp, self._unitDown)
        else:
            print ("Errore stai sottraendo mele e banane")
            return Data(0, 0, " ", " ")

    def __mul__(self, other):
        newValue = self._value * other._value
        newError = newValue * (self.getRelError() + other.getRelError())
        newUp = self._unitUp + other._unitUp
        newDown = self._unitDown  + other._unitDown
        return Data(newValue, newError, newUp, newDown)

    def __truediv__(self, other):
        newValue = self._value / other._value
        newError = newValue * (self.getRelError() + other.getRelError())
        newUp = self._unitUp + other._unitDown
        newDown = self._unitDown  + other._unitUp
        return Data(newValue, newError, newUp, newDown)
