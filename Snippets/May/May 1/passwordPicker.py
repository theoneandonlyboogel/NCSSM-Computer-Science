"""
challenge 1: give your program a clear beginning and end✓
challenge 2: add more words to add complexity
challenge 3: change the code so the program will create and display at three passwords at once
challenge 4: make it longer- by adding another word into each password"""
import random
import string
import pyfiglet

order = []
for i in range(1,4):
    rand = random.randint(1, 4)
    if rand in order:
        continue
    else:
        order.append(rand)
        i += 1


adjectives = [
    "conventional",
    "enthusiastic",
    "mathematical",
    "unreasonable",
    "intellectual",
    "geographical",
    "presidential",
    "quagmireous",
    "outrageous",
    "unacceptable"
]

nouns = [
    "discrimination",
    "sophomore",
    "sophistication",
    "reorganization",
    "implementation",
    "vice-president",
    "reconciliation",
    "reconstruction",
    "rehabilitation",
    "macroeconomics"
]

print(pyfiglet.figlet_format("Password Picker",font= "chunky"))
while True:
    qty = int(input("How many passwords? "))
    for i in range(0, qty):
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100000)
        specialChar = random.choice(string.punctuation)

        adjNoun = adjective + "_" + noun

        order = []
        while len(order) < 3:
            t = random.randint(1, 3)
            if t not in order:
               order.append(t)
               i+1
            else:
               continue
            fullString = "".join(str(order)).replace("[", "").replace("]", "").replace(",", "")
        password = str(fullString.replace("2", adjNoun).replace("1", specialChar).replace("3", str(number)).replace(" ", ""))
        print(password)
        i += 1
    userInput = input("Would you like another password? Type Y/n ").lower()
    if userInput == "n":
        print(pyfiglet.figlet_format("Cya!",font= "chunky"))
        break
    if userInput == "y":
        continue
