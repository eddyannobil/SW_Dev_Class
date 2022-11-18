#!/usr/bin/env python3
def input_func():
    """Receives user's input of name and list of random numbers

    Args:
        None

    Return:
        name(string): The user's name
        user_list(string): User's list of random numbers

    Raise:
        None
    """
    name = input("What is your name?")
    user_input = input("Enter a list of random numbers separated by a comma:")
    user_list = user_input.split(",")
    return (name,user_list)

def james_bond():
    """Calls input func function and loops through the return to identify 0,0,7

    Args:
        None

    Return:
        name(string): The user's name
        Boolean: True/False

    Raise:
        None
    """
    user_list = input_func()
    list = user_list[1]
    name = user_list[0]
    print(list)
    
    for idx, num in enumerate(list):
        if len(list) >= 3:
            if idx == len(list)-1:
                return (name,False)
            if num == '0'and list[idx+ 1] == '0' and list[idx + 2] == '7':
                return (name,True)   
            else:
                continue 
        else:
            return (name,False) 
    
def results():
    """Calls the james_bond function and prints output based on the return of the function

    Args:
        None

    Return:
        None

    Raise:
        None
    """
    output = james_bond()
    output_name = output[0]  
    output_condition = output[1]
    if output_condition == True:
        print(f'{output_name} is qualified to be James Bond!')
    else:
        print(f'{output_name} is not qualified to be James Bond!')    

def main():
    """Calls results function to display if the user is qualified to be James Bond

    Args:
        None

    Return:
        None

    Raise:
        None
    """
    results()

if __name__ == "__main__":
    main()
