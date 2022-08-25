#!/usr/bin/env python3
'''
This script computes the actual sum of the five "random" four-digit numbers 
to cross-check with the predicted sum and display the result to the user.
'''

# A variable is declared to store the user's name and input number
user = input("What is your name? ")
print(f"Hello {user}, do you believe in mathemagic? ")
random_no = input("Enter a 4 digit random number:")

# Conditions are set to ensure the user selects numbers that are valid in our code
if random_no.isnumeric():   
    if int(random_no) == 0000:
        print(f"{random_no} is not a valid number")
        random_no = input("Please enter a valid 4 digit number greater than zero:")
        
    if int(random_no) <= 999 and int(random_no) != 0:
        print(f"{random_no} is not a 4 digit number")
        random_no = input("Please enter a valid 4 digit number that doesn't start with zero:")
  
    if int(random_no) > 9999:
        print(f"Your number has {len(random_no)} digits")
        print(f"{random_no} is not a valid four-digit number")
        random_no = input("Please enter a valid 4 digit number:")

    if int(random_no) == 9999:
        print(f"The algorithm does not support {random_no}")
        random_no = input("Please enter another valid 4 digit number:")    

    if int(random_no) > 0 and int(random_no) < 9999 and int(random_no[0]) > 0:
        print("That is a valid number")
        random_number = int(random_no) - 2  

        if random_number < 1000:
            random_num = ('20' + str(random_number))
        else:
            random_num = ('2' + str(random_number)) 
        # The sum of all random numbers is predicted at the start of the first input            
        print(f"The sum of all the numbers you will enter will be {random_num}")    
        random_no2 = input("Enter another 4 digit number:")
        # A second random number is received if it is valid 
        if random_no2.isnumeric():   
            if int(random_no2) == 0000:
                print(f"{random_no2} is not a valid number")
                random_no2 = input("Please enter a valid 4 digit number greater than zero:")
            
            if int(random_no2) <= 999 and int(random_no2) != 0:
                print(f"{random_no2} is not a 4 digit number")
                random_no2 = input("Please enter a valid 4 digit number that doesn't start with zero:")

            if int(random_no2) > 9999:
                print(f"Your number has {len(random_no2)} digits")
                print(f"{random_no2} is not a valid four-digit number")
                random_no2 = input("Please enter a valid 4 digit number:")

            if int(random_no2) == 9999:
                print(f"The algorithm does not support {random_no2}")
                random_no2 = input("Please enter another valid 4 digit number:")      

            if int(random_no2) > 0 and int(random_no2) < 9999 and int(random_no2[0]) > 0:
                print("That is a valid number")
                nine_minus_random1 = str(9 - int(random_no2[0])) 
                nine_minus_random2 = str(9 - int(random_no2[1]))
                nine_minus_random3 = str(9 - int(random_no2[2]))
                nine_minus_random4 = str(9 - int(random_no2[3]))
                nine_minus_random_a = nine_minus_random1 + nine_minus_random2 + nine_minus_random3 + nine_minus_random4
                print(f"Ok, my number will be {nine_minus_random_a}")
        else:
            print(f"{random_no2} is not a number") 

        random_no3 = (input("Enter another 4 digit number:"))
        # A third random number is received if it is valid        
        if random_no3.isnumeric():   
                if int(random_no3) == 0000:
                    print(f"{random_no3} is not a valid number")
                    random_no3 = (input("Please enter a valid 4 digit number greater than zero:"))

                if int(random_no3) <= 999 and int(random_no3) != 0:
                    print(f"{random_no3} is not a 4 digit number")
                    random_no3 = (input("Please enter a valid 4 digit number that doesn't start with zero:"))
  
                if int(random_no3) > 9999:
                    print(f"Your number has {len(random_no3)} digits")
                    print(f"{random_no3} is not a valid four-digit number")
                    random_no3 = (input("Please enter a valid 4 digit number:"))

                if int(random_no3) == 9999:
                    print(f"The algorithm does not support {random_no3}")
                    random_no3 = input("Please enter another valid 4 digit number:")      

                if int(random_no3) > 0 and int(random_no3) < 9999 and int(random_no3[0]) > 0:
                    print("That is a valid number")
                    nine_minus_random5 = str(9 - int(random_no3[0])) 
                    nine_minus_random6 = str(9 - int(random_no3[1]))
                    nine_minus_random7 = str(9 - int(random_no3[2]))
                    nine_minus_random8 = str(9 - int(random_no3[3]))
                    nine_minus_random_b = nine_minus_random5 + nine_minus_random6 + nine_minus_random7 + nine_minus_random8
                    print(f"Ok, my number will be {nine_minus_random_b}")
                    print(f"So far, the numbers we have are: {random_no}, {random_no2}, {nine_minus_random_a}, {random_no3}, {nine_minus_random_b}")
                    print("Take a sec to compute the sum of these numbers...")
                    sum_of_4 = int(random_no) + int(random_no2) + int(random_no3) + int(nine_minus_random_a) + int(nine_minus_random_b)
                    # The sum of all 5 random numbers is predicted                     
                    print(f"Did you get {sum_of_4}?")
                    print("It's mathemagic!")
        else:
            print(f"{random_no3} is not a number") 
else:
    print(f"{random_no} is not a number") 
