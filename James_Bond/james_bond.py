#!/usr/bin/env python3
name = input("What is your name?")
user_input= input("Enter a list of random numbers separated by a comma:")
user_list = user_input.split(",")

for idx, num in enumerate(user_list):
    if len(user_list) >= 3:
        if idx == len(user_list)-1:
            print(f'{name} is not qualified to be James Bond!')
        if num == '0'and user_list[idx+ 1] == '0' and user_list[idx + 2] == '7':
            print(f'{name} is qualified to be James Bond!')
            break
        else:
            continue 
    else:
        print(f'{name} is not qualified to be James Bond!')
        break
    
                
            

  



  
    


