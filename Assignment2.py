"""'
Task 1: Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.
"""

user_first_name = input("Please enter your first name: ")
user_last_name = input("Please enter your last name: ")

if len(user_first_name) < 2:
    print("Your first name is not long enough, please try again")
    try_again = input("Please enter your first name: ")

if len(user_last_name) < 2:
    print("Your last name is not long enough, please try again")
    try_again = input("Please enter your last name: ")

print(f"Welcome {user_first_name} {user_last_name}!")
