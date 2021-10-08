def duplicate_encode(word):
    #your code here
    word = word.lower()
    word_array = [char for char in word]
    encoder = ''
    
    for i in range(len(word_array)):
        char_count = word_array.count(word_array[i])
        if char_count == 1:
            encoder += '('
        else:
            encoder += ')'
            
    return encoder

#
def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])