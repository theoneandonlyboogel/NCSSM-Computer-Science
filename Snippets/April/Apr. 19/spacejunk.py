#idea is to have a space junk dodging game with live timers on one side, something else on the other side that i need to figure out but also needs to be interactive
import time #for timing inputs in the debris section
import pyfiglet #for ascii art
from inputimeout import inputimeout, TimeoutOccurred #idk if ill use this




completed = False
spaceFrame1 = """                                 
        _____                                                               +
    ,-:` \;',`'-,                       *                       
  .'-;_,;  ':-;_,'.                                                                                     '
 /;   '/    ,  _`.-\                                            '       
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |           *                                                                   +
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'                                                         '
    `'-._____. '                                        
                            +

    *                                       '                 
                                                                                            '  """
spaceFrame2 = """
"""
spaceText1 = """
Welcome to Earth's orbit. The year is 2456, and humans have achieved intergalactic travel. You are on a mission to Earth for some
long lost relics, and finishing this mission will give you a promotion back at your trade center. The only problem is, there is a 
massive debris cloud surrounding the planet, due to its use as a missile test site. You must avoid the space junk to make it to Earth
and complete your mission.
Do you wish to fly around Earth to avoid the largest cluster of space debris, or are you going to fly straight into the cloud and
avoid the debris, so you can get a time bonus on your mission?
Enter either 1 to fly around Earth, or 2 to fly straight into the debris cloud. """
gameOver = pyfiglet.figlet_format("GAME OVER",font= "isometric3")
gameWon = "you won"

def intro():
    intro = pyfiglet.figlet_format("Space Junk",font= "isometric3")
    print(f"{intro}\n\nA Choose Your Own Adventure game, where you propel yourself off of different space objects to reach you endgoalreplacelater\nPress Enter to begin. ", end="")
    start = input("")
    if start != "":
        exit()
    else:
        return True


def debrisPath(sequence, timer):
    while True:
        print(f"Input --> {sequence} <-- in the next {timer} seconds to dodge the space junk.")
        userInput = inputimeout(prompt="", timeout=timer)
        if userInput == sequence:
            print("Nice! You dodged the space junk!")
            time.sleep(1)
            return True
        if userInput != sequence and TimeoutOccurred == False:
            continue
        if TimeoutOccurred:
            print(gameOver)
            break
        

    
def pathAround():
    print("You have chosen to fly around Earth. However, your ship's treasurer has miscalculated the amount of fuel you have left, and \nwithout some drastic measures, you won't be able to make it to Earth in time. Get ready to make some difficult choices.")
    time.sleep(5)
    userInput = input("")






    
def main():
    if intro() == True: 
        choice1 = int(input(f"{spaceFrame1}\n{spaceText1}"))
        if choice1 == 2:
            print("You have chosen the debris path. Get ready to dodge space junk.")
            time.sleep(4)
            if debrisPath("low", 4) == True:
                print("You continue your flight rapidly towards the Earth, but another piece of space junk found itself in your path. \nGET READY TO DODGE!")
                time.sleep(5)
                if debrisPath("up", 3) == True:
                    print("You're almost to the landing pad, but yet another piece of space junk crosses your path. It's now or never: TIME TO DODGE!")
                    time.sleep(5)
                    if debrisPath("right", 5) == True:
                        print(gameWon)
        elif choice1 == 1:
            pathAround()
            
        
        else:
            print("Try again.")


            


            

    
main()

#some ascii art has been copied from https://www.asciiart.eu/space/



"""
def debrisPath(sequence, timer):
    start_time = time.time()  # Record the start time
    while True:
        remaining_time = timer - (time.time() - start_time)
        if remaining_time <= 0:
            print(f"\n{gameOver}")
            break
        try:
            user_input = input(f"You have {round(remaining_time, 1)} seconds until a large piece of debris collides with your ship!\nEnter {sequence} to avoid the debris: ", end="\r")
            if user_input == sequence:
                return True
            else:
                print(gameOver)
                break
        except TimeoutOccurred:
            pass  # Continue the loop if no input is received within the timeout period"""
