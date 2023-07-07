# Quiz game in Python
print("Welcome to Quiz Game!")

playing = input("\nDo you want to play?\n[Y] Yes\n[N] No\n: ")

if playing.lower() != "y":
    quit()

print("Lets play:\n")

# Questions array
questions = [
    "What is the full form of CPU?\n: ",
    "What is the name for a portable computer input device that moves the cursor on the screen?\n: ",
    "What is the full form of GPU?\n: ",
    "What is the term for a computer input device that allows users to enter text and commands?\n: ",
    "What is the full form of RAM?\n: ",
    "What is the term for a computer's main circuit board that holds essential components?\n: ",
    "What is the full form of ROM?\n: ",
    "What is the term for the physical components of a computer that can be seen and touched?\n: ",
    "What is the full form of URL?\n: ",
    "What is the name for a small data file stored on a user's computer by a website to remember preferences or login information?\n: ",
]

# Answers array
answers = [
    "central processing unit",
    "mouse",
    "graphics processing unit",
    "keyboard",
    "random access memory",
    "motherboard",
    "read only memory",
    "hardware",
    "uniform resource locator",
    "cookie",
]

score = 0

# For loop to go through each questions
for question in questions:
    answer = input(f"{question}")
    if answer.lower() == answers[questions.index(question)]:
        print("Correct answer!\n")
        score += 1
    else:
        print("Incorrect answer!\n")

# Result
print(f"You got {str(score)} question correct.")
print(f"You got {str(((score)/10)*100)}% question correct.")
