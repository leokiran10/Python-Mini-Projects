import random

top_of_range= input("\nType maximum limit of number upto which you want to guess: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    total_guess=0

    if top_of_range<=0:
        print("Please type a number larger than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()


random_number=random.randint(1,top_of_range)

while True:
    total_guess+=1
    user_guess= input("Guess any number: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    
    if user_guess==random_number:
        print("You got it :)\n")
        break
    elif user_guess>random_number:
        print("You were above the number!\n")
    else:
        print("You were below the number!\n")

print("You got correct answer in",total_guess,"guesses.\n")


