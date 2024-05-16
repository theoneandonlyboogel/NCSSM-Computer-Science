import time

#animal quiz intro
print("Welcome to the animal quiz. Inputs are case and space insensitive.")

#open ended question, 3 guesses
def openQuestion(prompt, answer):
    global score
    attemptsRemaining = 3
    while attemptsRemaining != 0:
        if input(prompt).strip().lower() == answer:
            score += attemptsRemaining
            print(f"Correct!\nYour score is {score}!")
            break
        else:
            attemptsRemaining -= 1
            print(f"Incorrect!\nTry again! You have {attemptsRemaining} attempts left.")
            
    if attemptsRemaining == 0:
        score -= 2
        print(f"Too many guesses!\nYour score is {score}!")
    return score

def multipleChoice(prompt, A, B, C, D, correctAnswer):
    #only one attempt b/c multiple choice is more forgiving, 3 points rewarded like normal questions. Lists are just for fancy animations.
    #(basically the entire time module is used for making the usage of the program cooler)
    answers = [A, B, C, D]
    headers = ["A: ", "B: ", "C: ", "D: "]
    global score
    print(prompt)
    for i in range(len(answers)):
        time.sleep(.5)
        print(f"{headers[i]}{answers[i]}")
        i += 1
    time.sleep(1.5)
    userInput = input("What's your answer? ").strip().lower()
    if userInput == correctAnswer:
        score += 3
        print(f"Correct!\nYour score is {score}!")
    else:
        score -= 1
        print(f"Incorrect!\nYour score is {score}!")
    return score

def trueFalse(prompt, answer):
    #True False question, one guess
    global score
    print(f"True or false: {prompt}")
    time.sleep(1.5)
    userInput = input("What's your answer? ").strip().lower()
    if userInput == answer:
        score += 2
        print(f"Correct!\nYour score is {score}!")
    else:
        score -= 1
        print(f"Incorrect!\nYour score is {score}!")
    return score


score = 0

def main():
    #calling each function with their arguments
    trueFalse("Cheetas roar, like all big cats.", "false")
    openQuestion("What has webbed feet, quacks like it's always gossiping, and enjoys swimming? ", "duck")
    trueFalse("Sea otters have favorite rocks they use to crack open their food with.", "true")
    multipleChoice("What is super spikey, lives in the ocean, and is similar to street urchins? ", "Hedgehog", "Sea Urchin", "Sea Anenome", "Rat", "b")
    openQuestion("What is massive, has a trunk but no keys, and is afraid of mice? ", "elephant")
    trueFalse("Dogs sneeze whenever they're playing to indicate that they aren't having fun and want to stop.", "false")
    openQuestion("What animal has stripes, can go from 0-60 in under 10 seconds, and is the mascot of a corn puffs brand? ", "cheeta")
    multipleChoice("What do you call a group of owls?", "Troop", "Clutter", "Smack", "Paraliment", "d")
    print(f"You finished the quiz!\nYour final score was {score}/21 questions correct.")



main()