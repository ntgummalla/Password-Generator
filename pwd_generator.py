import random
import string

def generate_pwd(min_len, numbers=True, special_char=True): # for pwd to include numbers and special chars.
    letters = string.ascii_letters # to access all the alphabets
    digits = string.digits # to access all numbers
    spc_chars = string.punctuation # to access all special characters

    chars = letters
    if numbers: #if numbers=True is True then add digits(w=str) to letters(str)
        chars += digits

    pwd = ""  # to store the pwd
    meets_criteria = False # will be set to true once pwd meets the criteria(1 number, 1 spc-char and min length)
    has_num = False # checking for a number(initially it's falsse as there's no number)
    has_spc_char = False # checking for a spc-char(initially it's falsse as there's no spc-char) 
    
    while not meets_criteria or len(pwd) < min_len: # loop to generate a new char to add to our random pwd until cond is false
        new_char = random.choice(chars) # pciks a random char
        pwd += new_char

        if new_char in digits:
            has_num = True
        elif new_char in spc_chars:
            has_spc_char = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_num
        if special_char:
            meets_criteria = meets_criteria and has_spc_char # if has_num is false, then meets-criteria should be also false

    return pwd

min_len = int(input("Enter the minimum length: "))
has_num = input("Do you want password to contain numbers? (yes/no) ").lower() == "yes" # returns a bool
has_spc_char = input("Do you want password to contain special characters? (yes/no) ") == "yes" #returns a bool

pwd = generate_pwd(min_len, has_num, has_spc_char)
print("The deisred password is: ", pwd)



