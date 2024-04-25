import time

#animal quiz
print("Welcome to the animal quiz. Inputs are case and space insensitive.")


def questionaire(prompt, answer):
    global score
    attempts = 0
    while attempts != 3:
        if input(prompt).strip().lower() == answer:
            score += 1
            print(f"Correct!\nYour score is {score}!")
        else:
            attempts += 1
            print(f"Incorrect!\nTry again! You have {3-attempts} attempts left.")
            
    if attempts == 3:
        score -= 1
        print(f"Too many guesses!\nYour score is {score}")
    return score

score = 0

def main():
    questionaire("What has webbed feet, quacks like it's always gossiping, and enjoys swimming? ", "duck")
    questionaire("What is massive, has a trunk but no keys, and is afraid of mice? ", "elephant")
    questionaire("What animal has stripes, can go from 0-60 in under 10 seconds, and is the mascot of a corn puffs brand? ", "cheeta")



main()