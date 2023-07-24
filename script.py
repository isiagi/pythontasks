# 1 Create a function named print_numbers().

# def print_numbers():
#     print(5)
#     print(100)

# print_numbers()
# print_numbers()

# 2 Write a program to check if the student passed or failed his/her examination by creating a function..

# user_input = input("Enter Marks Please: ")

# def checkMarks(user_inputz):
    
#     try:
#         int_marks = int(user_inputz)
#     except:
#         print("Unable to convert user input to integer")
#         return
        
#     if (int_marks >= 70):
#         print("Pass")
#     else:
#         print("Fail")

# checkMarks(user_input)

# 3. Write a program to check if the two arguments passed are equal or not by creating a function.

# def my_function(num1, num2):
#     if (num1 == num2):
#         print(True)
#     else:
#         print(False)

# my_function(1, "1")

# 4. Write a program to print full name with space in between using a function.

# def full_name(first_name, last_name):
#     if (isinstance(first_name, str) and isinstance(last_name, str)):
#         print(first_name + " " + last_name)
#         return
        
#     print("Inputs must be strings!")
#     return

# full_name("Geofrey", 90)
    
# 5. Write a program to check whether a number is prime or not using a function.

# def check_prime(num):
#     flag = False

#     if(num == 1):
#         print("1 is not a prime number")
#     elif num > 1:
#         for i in range(2, num):
#             print(i)
#             if (num % i ) == 0:
#                 flag = True
#                 break
        
#     if flag:
#         print(num, "Is not prime")
#     else:
#         print(num, "Is prime number")
                
        

# check_prime(6)

# Intermediate

# 6. Write a program to calculate the power of an integer using a function.

# num = input("Enter Number: ")

# flag = False

# try:
#     num_marks = int(num)
# except:
#     flag = True

# def calculate_pow(arg1):
#     print(arg1 ** 3)

# if flag:
#     print("Unable to convert user input to integer")
# else:
#     calculate_pow(num_marks)