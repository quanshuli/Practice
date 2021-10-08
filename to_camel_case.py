def to_camel_case(text):
    #your code here
    import re
    text.lower()
    
    #set the delimiters
    text1 = re.split('[-_ .]', text)
    
    #the first word doesnt need to be upper case
    text2 = text1[0]
    
    for i in range(1,len(text1)):
        
        #use capitalize to make the first char upper case
        text2 += text1[i].capitalize()
    
    return text2
    
    