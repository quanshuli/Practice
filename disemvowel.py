# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:03:14 2021

@author: peace
"""

def disemvowel(string_):
    import re
    newString = re.sub(r'[aeiouAEIOU]', '', string_)
    return newString


test = "This website is for losers LOL!"

print(disemvowel(test))