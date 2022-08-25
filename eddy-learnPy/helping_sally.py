#!/usr/bin/env python3
business_name = "Sally's Fruity Loops"

#This is the list of all the fruits I'll be selling

fruit_list = ["Apple", "Banana", "Cherries", "Dragon Fruit", "Fig",
               "Grapefruit", "Kiwi", "Lemon", "Lime", "Mango", "Oranges", "Pineapple",
              "Grapes", "Watermelon"]

#This is the list of the prices of each fruit in the fruit list.

fruit_prices_list = [ 1.35, 1.30, 0.32, 0.60, 0.80, 1.76, 3.32, 0.34, 2, 3, 2.46, 1.43,
                      1.8, 1.9]

# Check if the first item in the fruit list is apple and then display
# a notice to customers.

if fruit_list[0] == "Apple": 
 print("Sally sells apples too!")


# Calculate how much discount to give customers on opening day
# by adding the prices of the first 2 fruits, divide by 100 and
# multiply by 5
discount_price = 0
discount_amount = (1.35 + 1.30 / 100) * 5
discount_percent = discount_price
print("Thanks for being a valued customer! Your discount is: ", discount_percent, "%")

#The code below will be used to show customers a list of random fruits on sale.

first_sample_from_fruit_list = fruit_list[1]
second_sample_from_fruit_list = fruit_list[13]
third_sample_from_fruit_list = fruit_list[9]
fourth_sample_from_fruit_list = fruit_list[7]
fifth_sample_from_fruit_list = fruit_list[10]

print("Here are the fruits on sale today:")
print(first_sample_from_fruit_list)
print(second_sample_from_fruit_list)
print(third_sample_from_fruit_list)
print(fourth_sample_from_fruit_list)

#This is a list of the first three fruits. I'll give these for free on my birthday

(fruit_1, fruit_2, fruit_3) = (fruit_list[1],fruit_list[2],fruit_list[3])
print(fruit_1, fruit_2, fruit_3)

#Declare a variable to store a customer's shopping cart total BEFORE they start shopping'

customer_total = 0

# This is the raw string that will be displayed on the homepage of the store's website
# The website can process newline characters (\n) and turn them into smiley faces,
# so we'll need those to show when the string is printed

raw_welcome = "Welcome to Sally's \n fruity loop store"
print(raw_welcome)

#Check that the customer cart total works properly by testing the cart total functionality

customer_total = customer_total + 10
print(customer_total)

# Declare a string to thank a customer for shopping and show them their cart total
# after ordering:

goodbye_msg = "Thanks for shopping at Sally's Fruity Loops"
print("Your total for today is:", customer_total)