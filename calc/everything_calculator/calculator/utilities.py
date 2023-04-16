"""Contains logic for using a calculator object.
"""


def get_user_input(calc_type):
    user_input = input(
        "Enter a list of comma-separated numbers followed by any of the following words: add, subtract, multiply or divide: "
    )
    user_list = user_input.split(",")  # 1,2,3,4,add -> ["1", "2", "3,", "4", "add"]
    user_numbers = user_list[0 : len(user_list) - 1]  # ["1", "2", "3,", "4"]
    operator = user_list[len(user_list) - 1]

    number_val, operator_val = validate_user_input(user_numbers, operator)
    if number_val == True and operator_val == True:
        fin_list = prepare_user_input(user_numbers)
        perform_calculation(fin_list, operator, calc_type)
    else:
        # TODO: Where should this return value be used?
        return "You entered invalid input! Try again!"


def validate_user_input(numbers, operator):
    # TODO: The validate_user_input function isn't checking for blank operators
    for num in numbers:
        if num.isdigit():
            num_validation = True
        else:
            num_validation = False

    if operator in ["add", "sub", "divide", "multiply"]:
        op_validation = True
    else:
        op_validation = False

    return num_validation, op_validation


def prepare_user_input(string_list):
    final_list = []
    for entry in string_list:
        final_list.append(int(entry))
    return final_list


def perform_calculation(some_list, some_operator, calc_type):
    if some_operator == "add":
        res = calc_type.add(some_list)
    elif some_operator == "sub":
        res = calc_type.subtract(some_list)
    elif some_operator == "multiply":
        res = calc_type.multiply(some_list)
    else:
        res = calc_type.divide(some_list)
    return display_result(res)


def sort_user_list(final_list):
    
    # TODO: Implement this such that the user list is sorted in ascending order before
    # used in calculation.

    result = []
    total = 0
    for num in final_list:
        if num >=0:

         pass


def display_result(result):
    # TODO: The output should be: The result of your ___ operation is ___.
    print(f"The result is {result}")
