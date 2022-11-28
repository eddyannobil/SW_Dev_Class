########################## Example Problems ##########################

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False

def makes_twenty(num1, num2):
    if (num1 + num2 == 20) or num1 == 20 or num2 == 20:
        return True
    else:
        return False

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(string):
    for idx, letter in enumerate(string):
        if letter == " ":
            if string[idx + 1] == string[0]:
                return True
            else:
                return False


# MASTER YODA: Given a sentence, return a sentence with the words reversed

# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'

def master_yoda(string):
   string_list = string.split(" ")
   #string_list = ["I", "am", "home"]
   final_string = ""
   for index in range(len(string_list)-1, -1, -1):
        final_string = final_string + string_list[index] + " "
        print(final_string) 
   print(final_string)     


# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(string):
    word = ""
    for letter in string:
        word = word + letter + letter + letter
    print(word)        
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'


# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'.
# NOTE: You must use a loop in your function, and you are not allowed to check if a number is 11 just
# by doing number == 11 :)

def blackjack(num1, num2, num3):
    list = [num1, num2, num3]
    print(list)
    sum = num1 + num2 + num3
    
    for num in list:
        if sum <= 21:
            return sum
     
        
        if 11 in list:
            if sum > 21:
                sum -= 10
                if sum > 21:
                    return "BUST"
                else:
                    return sum

        if 11 not in list:
            if sum > 21:
                return "BUST"
        #          return "BUST" 
    
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19


def main():
    # prob1_res1 = makes_twenty(20, 10)  # True
    # prob1_res2 = makes_twenty(12, 8)  # True
    # prob1_res3 = makes_twenty(2, 3)  # False
    # print(prob1_res1, prob1_res2, prob1_res3)

    # prob2_res1 = animal_crackers("Levelheaded Llama")  # True
    # prob2_res2 = animal_crackers("Crazy Kangaroo")  # False
    # print(prob2_res1, prob2_res2)

    # master_yoda("I am home")
    # master_yoda("We are ready")
    #paper_doll('Mississippi')
    result = blackjack(9,9,11)
    print(result)

if __name__ == "__main__":
    main()
