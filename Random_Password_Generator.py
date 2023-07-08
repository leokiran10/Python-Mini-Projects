# Importing libraries
import random
import string

# generate_password() function


def generate_password(length, numbers, special_characters):
    # Strings
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""

    while len(pwd) < length:
        if len(pwd) == 0:
            new_char = random.choice(letters)
            pwd += new_char
        elif len(pwd) == 1 and has_number:
            new_char = random.choice(digits)
            pwd += new_char
        elif len(pwd) == 2 and has_special:
            new_char = random.choice(special)
            pwd += new_char
        else:
            new_char = random.choice(characters)
            pwd += new_char

    # Shuffled list
    pwd_list = random.sample(pwd, len(pwd))
    # Shuffled list -> String
    shuffled_pwd = ''.join(pwd_list)

    return shuffled_pwd


length = int(input("Enter the length of the password: "))
has_number = input("Do you want to have numbers (yes/no)? ").lower() == "yes"
has_special = input(
    "Do you want to have special characters (yes/no)? ").lower() == "yes"
password = generate_password(length, has_number, has_special)
print("The generated password is:\n", password)

