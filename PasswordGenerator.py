import random

chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+-=\/?><,."

while 1: 
    password_len = int(input("How long should the password be? : "))
    password_count = int(input("How many passwords would you like? : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Here is your password :", password)

            