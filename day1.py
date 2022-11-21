#################
# Day 1 of 50
# Write a function called divide_or_square that takes one argument
# (a number) and returns the square root of the number if it is divisible by 5,
# returns the remainder if it is not divisible by 5.
#
# For example, if you pass 10 as an argument, then your function should return 3.16 as the square root
################

# Import functions
import math

# Define your function

def divide_or_square(num):
    """
    Take the argument and return the following:
        * Square root of the number if it is divisible by 5
        * Remainder if it is not divisible by 5
    """
    if num % 5 == 0:
        return format(math.sqrt(num),'.2f')
    else:
        return num % 5

# Execute function with input

prompt = ''

while prompt.lower() != 'no':
    user_input = int(input('\nPlease input a number: '))
    print(divide_or_square(user_input))
    prompt = input('Continue? Yes or No: ')

input('\nPress ENTER to exit')

