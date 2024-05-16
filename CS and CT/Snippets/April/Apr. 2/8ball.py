#ifthen, class demonstration
import random
import pyfiglet

print(pyfiglet.figlet_format("The Magical 8-Ball"))

responses = [
    "It is certain.",
    "Without a doubt.",
    "You may rely on it.",
    "Yes, definitely.",
    "It is decidedly so.",
    "As I see it, yes.",
    "Most likely.",
    "Yes.",
    "Outlook good.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Better not tell you now.",
    "Ask again later.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "Outlook not so good.",
    "My sources say no.",
    "Very doubtful.",
    "My reply is no."
]
while True:
    question = input("Ask the Magical 8-ball a question (or press enter to quit). ")
    if question == "":
        break
    #generate random number to coorespond to index of list
    randIndex = random.randint(0, len(responses) -1)
    if randIndex < 10:
        print("The Magical 8-ball says:", responses[randIndex])
    elif randIndex < 15:
        print("The Magical 8-ball is uncertain:", responses[randIndex])
    else:
        print("The Magical 8-ball is doubtful:", responses[randIndex])