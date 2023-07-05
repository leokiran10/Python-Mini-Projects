print("Welcome to Quiz Game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Lets play:\n")

score = 0
# Question no. 1
answer = input("What is the full form of CPU? ")
if answer.lower() == "central processing unit":
    print("Correct answer!\n")
    score += 1
else:
    print("Incorrect answer!\n")

# Question no. 2
answer = input(
    "What is the name for a portable computer input device that moves the cursor on the screen? ")
if answer.lower() == "mouse":
    print("Correct answer!\n")
    score += 1
else:
    print("Incorrect answer!\n")

# Question no. 3
answer = input("What is the full form of GPU? ")
if answer.lower() == "graphics processing unit":
    print("Correct answer!\n")
    score += 1
else:
    print("Incorrect answer\n!")

# Question no. 4
answer = input(
    "What is the term for a computer input device that allows users to enter text and commands? ")
if answer.lower() == "keyboard":
    print("Correct answer!\n")
    score += 1
else:
    print("Incorrect answer\n!")

# Question no. 5
answer = input("What is the full form of RAM? ")
if answer.lower() == "random access memory":
    print("Correct answer!\n")
    score += 1
else:
    print("Incorrect answer!\n")

# Question no. 6
answer = input(
    "What is the term for a computer's main circuit board that holds essential components? ")
if answer.lower() == "motherboard":
    print("Correct answer!\n")
    score += 1
else:
    print("Incorrect answer!\n")

# Question no. 7
answer = input("What is the full form of ROM? ")
if answer.lower() == "Read only memory":
    print("Correct answer!\n")
    score += 1
else:
    print("Incorrect answer!\n")

# Question no. 8
answer = input(
    "What is the term for the physical components of a computer that can be seen and touched? ")
if answer.lower() == "hardware":
    print("Correct answer!\n")
    score += 1
else:
    print("Incorrect answer!\n")

# Question no. 9
answer = input("What is the full form of URL? ")
if answer.lower() == "uniform resource locator":
    print("Correct answer!\n")
    score += 1
else:
    print("Incorrect answer!\n")

# Question no. 10
answer = input(
    "What is the name for a small data file stored on a user's computer by a website to remember preferences or login information? ")
if answer.lower() == "cookie":
    print("Correct answer!\n")
    score += 1
else:
    print("Incorrect answer!\n")

# Result
print("You got "+str(score)+" question correct.")
print("You got " + str(((score)/10)*100) + "%" + " question correct.")
