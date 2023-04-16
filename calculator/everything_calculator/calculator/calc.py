""" Contains the definition for an everything calc
"""


class Calculator:
    # class atrributes
    brand = "EC"
    model = "5000"

    def __init__(self, serial_num):
        self.serial_num = serial_num
        self.starting_batt_percent = 100
        self.calculator_state = "on"  # on, off, dead

    def add(self, input_list):  # [1,2,3,4,5] -> 1 + 2 + 3 + 4 + 5
        result = 0
        for num in input_list:
            result += num
        self.starting_batt_percent -= 1
        return result

    def subtract(self, input_list):
        # TODO: Implement!
        total_diff = 0
        for result in input_list:
            result -= total_diff
        self.starting_batt_percent -= 1
        return result 


    def multiply(self, input_list):
        result = 1
        for num in input_list:
             result *= num 
        self.starting_batt_percent -= 1   
        return result



        # TODO: Implement!
        pass

    def divide(self,input_list):
        result = 1
        for num in input_list:
             result %= num 
        self.starting_batt_percent -= 1   
        return result 

        # TODO: Implement!
        pass

    def power_on(self):
        self.calculator_state = "on" 
        # TODO: Implement!
        pass

    def power_off(self):
        self.calculator_state = "off" 
        # TODO: Implement!
        pass

    def run_low_batt(self):
        if self.starting_batt_percent <= 10:
            print(f'Low Battery')  
        # TODO: Implement!

        pass

    def die(self):
        if self.starting_batt_percent == 0:
            self.calculator_state = "off"  
        # TODO: Implement!
        pass

    def display_battery_life(self):
        print(self.starting_batt_percent)
        # TODO: Implement!
        pass
