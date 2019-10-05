"""
File: data.py
Author: Davide Rolino
Last modified: 13/04/19
Class for a Physical data with: value, error
    for the moment the class will only work with maximum errors (not 3 sigma errors), also the formula for the propagation of the errors will be the ones approximate and not the one that involves the derivatives
"""

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

#invert(n) = -n -1
def make_func(name):
    #return lambda self, *args: Data(getattr(self._value, name)(*args), self._error)
    def func(self, *args):
        a = Data(self._value, self._error)
        if len(args) == 0:
            a._value = getattr(a._value, name)()
            return a
        for i in args:
            if not isinstance(i, Data):
                i = Data(i)
            a._value = getattr(a._value, name)(i._value)
            a._error += i._error
        return a
    return func     

for name in ["__add__", "__radd__", "__sub__", "__rsub__", "__mul__", "__rmul__", "__rtruediv__", "__truediv__", "__pow__", "__rpow__", "__neg__", "__pos__"]:
    setattr(Data, name, make_func(name))  


