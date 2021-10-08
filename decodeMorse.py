# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 20:50:42 2021

@author: peace
"""
MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    a = morse_code.split('   ')
    b = ''
    #print(a)
    for i in range(len(a)):
        if a[i] != '':
        
            #a[i] = a[i].rstrip()
            #a[i] = a[i].lstrip()
            a[i] = strip()
            #print(a[i])
            c = a[i].split(' ')
            #print(c)
            for j in range(len(c)):
                b += MORSE_CODE[c[j]]
                
            b += ' '
        
    b = b.rstrip()
    return b

print(decodeMorse('   .   . '))

#
def decodeMorse(morseCode):
    return ''.join(MORSE_CODE.get(x, ' ') for x in morseCode.split(' ')).strip().replace('  ', ' ')


