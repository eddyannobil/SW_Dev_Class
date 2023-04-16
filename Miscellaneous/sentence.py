# def sentence(words):


#     list_of_words = [ ]
#     phrase = ' '

#     for word in words:
#         list_of_words.append(word)

#     for idx, word in enumerate(list_of_words):
#         if word == 0:
#             word += '.'
#         else:    
#             print(idx, word)
#             #word += word[idx +1]
#     print(word)
#     # for word in range(len(list_of_words)):
#     # if word == 0;
#     #  word + "."
#     # word[pos] + word[] 
#     #     pass
# sentence("I am going to work")    

def sentence(word_list):
    #word_list = ['I', 'am', 'home']
    phrase = ''

    for word in word_list:
        phrase = phrase + word + " "
        

    phrase += '.'
    print(phrase)
sentence(['Where', 'are', 'you'])