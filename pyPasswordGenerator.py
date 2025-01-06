
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password?")
nr_letters = int(input("> "))
print("How many symbols would you like?")
nr_symbols = int(input("> "))
print("How many numbers would you like?")
nr_numbers = int(input("> "))

# Randomly selected characters
password_letters = random.choices(letters, k = nr_letters)
password_numbers = random.choices(numbers, k = nr_numbers)
password_symbols = random.choices(symbols, k = nr_symbols)

# Combine all characters
required_password = password_letters + password_numbers + password_symbols
# print(required_password)

# Mix all characters
random.shuffle(required_password)
# print(required_password)

# convert list into string
final_password = ""
for char in required_password:
    final_password = final_password + char
print(f"Your required password is: {final_password}")