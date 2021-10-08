# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 21:59:22 2021

@author: peace
"""

def to_jaden_case(string):
    # ...
    
    a = string.split(' ')
    b= ''
    for item in a:
        
        b += item.capitalize() + ' '
        
    b = b.rstrip()
    return b

quote = "How can mirrors be real if our eyes aren't real"

c = to_jaden_case(quote)  

# other methods
def toJadenCase(string):        
    return " ".join(w.capitalize() for w in string.split())

#
import string

def toJadenCase(NonJadenStrings):
    return string.capwords(NonJadenStrings)
#
from string import capwords as toJadenCase

