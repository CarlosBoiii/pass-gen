import string
import random

def pass_gen():

    s_l = string.ascii_lowercase
    s_u = string.ascii_uppercase
    s_d = string.digits
    s_p = string.punctuation

    # Empty list
    pass_list = []

    # Add chars to the list
    pass_list.extend(s_l)
    pass_list.extend(s_u)
    pass_list.extend(s_d)
    pass_list.extend(s_p)

    # Shuffle password list char
    random.shuffle(pass_list)

    # Get password length from user input
    pass_length = int(input("enter password length : "))

    # Convert password list to string from index 0 to password length from input
    password_result = "" .join(pass_list[0:pass_length])

    # Print password generated
    print("Your new password is : ", password_result)

# Call password generator function
pass_gen()



