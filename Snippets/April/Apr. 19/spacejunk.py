#idea is to have a space junk dodging game with live timers on one side, something else on the other side that i need to figure out but also needs to be interactive
import time #for timing inputs in the debris section
import pyfiglet #for ascii art
from inputimeout import inputimeout, TimeoutOccurred #idk if ill use this



#frames and general vars that are used for multiple functions, so I put them here
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
gameWon = """
           .       .                   .       .      .     .      .
          .    .         .    .            .     ______
      .           .             .               ////////
                .    .   ________   .  .      /////////     .    .
           .            |.____.  /\        ./////////    .
    .                 .//      \/  |\     /////////
       .       .    .//          \ |  \ /////////       .     .   .
                    ||.    .    .| |  ///////// .     .
     .    .         ||           | |//`,/////                .
             .       \\        ./ //  /  \/   .
  .                    \\.___./ //\` '   ,_\     .     .
          .           .     \ //////\ , /   \                 .    .
                       .    ///////// \|  '  |    .
      .        .          ///////// .   \ _ /          .
                        /////////                              .
                 .   ./////////     .     .
         .           --------   .                  ..             .
  .               .        .         .                       .
                        ________________________
____________------------                        -------------_________"""


def intro():
    #yes, I am aware that not entering enter just spams the terminal. Don't try it at home kids.
    #begins the shenenagins through introducing the game, and asking for the user to press enter. Once enter is pressed, it returns true, used in main().
    while True:
        intro = pyfiglet.figlet_format("Space Junk",font= "isometric3")
        print(f"{intro}\n\nA Choose Your Own Adventure game, where you dodge space objects or tightly manage your fuel to reach planet Earth before it runs out or you collide with space junk.\nPress Enter to begin. ", end="")
        start = input("")
        if start != "":
            continue
        else:
            return True

def debrisPath(sequence, timer):
    #no, this path didn't take me 4 days because i was trying to thread a timer and input at the same time but don't know how to do threads
    #asks for the user to input a sequence in less than the timer, using inputimeout module to determine that. if the user inputs said input, move on to the next one in the path determined in main()
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
    #procrastination is the devil's incarnation in all humans. (aka this took forever for me to get to)
    #idk i havent gotten here yet
    print("You have chosen to fly around Earth. However, your ship's treasurer has miscalculated the amount of fuel you have left, and \nwithout some drastic measures, you won't be able to make it to Earth in time. Get ready to make some difficult choices.")
    time.sleep(5)
    userInput = input("")

def main():
    #where the magic happens, and my if statement count doubles
    #asks the user for a choice between two paths, and commences the path. Each path has 3 decisions/inputs, and if all 3 are done within tolerance, gameWon screen is shown. else, gameOver is shown.
    if intro() == True: 
        while True:
            choice1 = input(f"{spaceFrame1}\n{spaceText1}")
            if choice1 == "2":
                print("You have chosen the debris path. Get ready to dodge space junk.")
                time.sleep(4)
                if debrisPath("low", 4) == True:
                    print("You continue your flight rapidly towards the Earth, but another piece of space junk found itself in your path. \nGET READY TO DODGE!")
                    time.sleep(5)
                    if debrisPath("up", 3) == True:
                        print("You're almost to the landing pad, but yet another piece of space junk crosses your path. It's now or never: TIME TO DODGE!")
                        time.sleep(5)
                        if debrisPath("right", 5) == True:
                            print(f"You avoided all of the debris, and no major damage was dealt to your ship.\nFine work.\n{gameWon}")
                            break
            elif choice1 == "1":
                pathAround()

            else:
                print("Try again.")
    
main()

#some ascii art has been copied from https://www.asciiart.eu/space/
