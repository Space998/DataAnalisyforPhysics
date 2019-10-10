"""
File: dataErr.py
Author: Davide Rolino
Class for a Physical data with: value, error
    for the moment the class will only work with maximum errors (not 3 sigma errors), also the formula for the propagation of the errors will be the ones approximate and not the one that involves the derivatives
"""

import math

class Data(object):
    def __init__(self, value, error = 0):
        self._value = value
        self._error = error

    def __repr__(self):
        return "Data({}, {})".format(repr(self._value), repr(self._error))

#methods to get class' parameters
    def get_Value(self):
        return self._value

    def get_Error(self):
        return self._error
    
#methods that work on class' parameters
    def get_RelError(self):
        return self._error/self._value

#override of standard methods
    def __str__(self): #print method.
        result = str(self._value) + " " + u"\u00B1" + " " + str(self._error)
        return result

#definition of math methods
    #definition of nth-sqare method
    def sqrt(self, n = 2):
        return Data(self._value ** (1/n), self._error)

    #definition of log_n method
    def log(self, n = math.e):
        if n == 2:
            return Data(math.log2(self._value), self._error)
        return Data(math.log(self._value, n), self._error)

#override of standard math methods
#invert(n) = -n -1
def make_func(name_func):
    #return lambda self, *args: Data(getattr(self._value, name)(*args), self._error)
    def func(self, *args):
        new_data = Data(self._value, self._error)
        if len(args) == 0:
            new_data._value = getattr(new_data._value, name_func)()
            return new_data
        for i in args:
            if not isinstance(i, Data):
                i = Data(i)
            new_data._value = getattr(new_data._value, name_func)(i._value)
            new_data._error += i._error
        return new_data
    return func     

for name_func in ["__add__", "__radd__", "__sub__", "__rsub__", "__mul__", "__rmul__", "__rtruediv__", "__truediv__", "__pow__", "__rpow__", "__neg__", "__pos__"]:
    setattr(Data, name_func, make_func(name_func))  

#ovverride of math mathods from math library
def make_math_func(name_math):
    def func(self):
        return Data(math_func[name_math](self._value), self._error)
    return func     

#default trigonometric function take in radiants
for name_math in ["cos", "acos", "sin", "asin", "tan", "atan", "cosh", "acosh", "sinh", "asinh", "tanh", "atanh", "exp", "expm1", "log1p"]:
    setattr(Data, name_math, make_math_func(name_math))   

math_func = {'cos': math.cos, 'acos': math.acos, 'sin' : math.sin, 'asin': math.asin, 'tan': math.tan, 'atan': math.atan, 'cosh': math.cosh, 'acosh': math.acosh, 'sinh': math.sinh, 'asinh': math.asinh, 'tanh': math.tanh, 'atanh': math.atanh, 'exp': math.exp, 'expm1': math.expm1, 'log1p': math.log1p }