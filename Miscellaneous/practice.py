def vowels(sentence):
    letter_a = 0
    letter_e = 0
    letter_i = 0
    letter_o = 0
    letter_u = 0

    #sentence = 'The boy is coming'
    for word in sentence:
        if  word == "a":
            letter_a += 1

        if word == 'e':
            letter_e += 1
        
        if word == 'i':
            letter_i += 1

        if word == 'o':
            letter_o += 1

        if word == 'u':
            letter_u += 1   

    result = { "Count of a" : letter_a, "Count of e" : letter_e, "Count of i" : letter_i, "Count of o" : letter_o, "Count of u" : letter_u }

    return result     
        
print(vowels('Do not come'))


        
