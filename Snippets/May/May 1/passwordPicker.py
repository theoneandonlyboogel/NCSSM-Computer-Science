import random
import string

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
adjective = random.choice(adjectives)
noun = random.choice(nouns)
number = random.randrange(0, 100000)
specialChar = random.choice(string.punctuation)




print(f"{adjective}\n{noun}\n{number}\n{specialChar}")

