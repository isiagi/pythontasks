# 1. Create a Python program to find the total number of special characters in a string. Use the following inbuilt Python
# functions:

import re

def total(word):
    pattern = r'[^a-zA-Z0-9\s]'

    special_characters = re.findall(pattern, word)

    print(len(special_characters))

total('hello! good morning *.')


# 2. Write a Python program that returns a string representation of numbers 1 to n.

def fizz_buzz(num):
    arr = []

    for digit in range(1, num + 1):
        if digit % 3 == 0:
            arr.append("fizz")
        elif digit % 5 == 0:
            arr.append("buzz")
        else:
            arr.append(digit)

    print(arr)

fizz_buzz(20)
            

# 4. Suppose you are in a restaurant with your friends. You get a bill of a certain amount.   

def share_bill(total_amount, friends):
    tax_rate =  8.875
    net_amount = (tax_rate / 100) * total_amount
    amount_per_each = (total_amount + net_amount) / friends

    print(amount_per_each)

share_bill(300, 6)

# 6. Write a Python program to find if the given number is a Harshad Number.
def add_num(num):
    count = 0

    output = [int(x) for x in str(num)]

    for item in output:
        count += item
    
    if(num % count == 0):
        print("It is a Harshad Number")
    else:
        print("It is a not Harshad Number")

add_num(18)

# 7. Write a program to find if the given number is an Armstrong Number.

def armstrong(num):
    count = 0
    output = [int(x) for x in str(num)]

    for item in output:
        count += item**3

    if (count == num):
        print("It is an Armstrong Number")
    else:
        print("It is an not Armstrong Number")

armstrong(371)   