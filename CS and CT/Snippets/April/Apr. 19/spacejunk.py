import time #for timing inputs in the debris section
import pyfiglet #for ascii art
from inputimeout import inputimeout, TimeoutOccurred #for choices in debrisPath
import random #for choices in pathAround


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
fuelGauge3 = """
  ________________
 /################\ 
|##################|
|##################|
|##################|
|##################|
|------------------|
|##################|
|##################|
|##################|
|##################|
|##################|
|------------------|
|##################|
|##################|
|##################|
|##################|
 \################/
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
fuelGauge2 = """
  ________________
 /                \     
|                  |
|                  |
|                  |
|                  |
|------------------|
|##################|
|##################|
|##################|
|##################|
|##################|
|------------------|
|##################|
|##################|
|##################|
|##################|
 \################/
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
fuelGauge1 = """
  ________________
 /                \     
|                  |
|                  |
|                  |
|                  |
|------------------|
|                  |
|                  |
|                  |
|                  |
|                  |
|------------------|
|##################|
|##################|
|##################|
|##################|
 \################/
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
fuelGauge0 = """
  ________________
 /                \     
|                  |
|                  |
|                  |
|                  |
|------------------|
|                  |
|                  |
|                  |
|                  |
|                  |
|------------------|
|                  |
|                  |
|                  |
|                  |
 \                /
  ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
stage1Text = """
You just embarked on your journey.
About 50 minutes on route, there is a celestial body that might influence your
path to Earth, but avoiding it right now would cost some fuel. Not avoiding it
would cost a lot of fuel.
Will you avoid the body right now and lose some fuel, or roll the dice, and have
a chance of using no fuel, or use a lot of fuel?


1 - Preemptively avoid the body    | 2 - Do nothing, roll the dice.
-1 Fuel Gauge slot                 | 50% chance for -0 Fuel Gauge Slots
(100% certainty)                   | 50% chance for -2 Fuel Gauge Slots

                          What's your choice?
                                   """
stage2Text = """
After avoiding the celestial body, you find yourself in outer Earth orbit.
While you chose the route with less space junk, there happens to be a massive
piece blocking your orbital path.
Avoiding it actively will cost some fuel. Not avoiding it will chance a collision
and could destroy your ship.


1 - Roll the dice.                 | 2 - Avoid the junk
60% chance for -0 fuel             | -1 Fuel Guage Slots
40% chance for a game over         | (100% certainty)  
                          What's your choice?
                                   """
stage3Text = """
You avoided a game ending collision, and you now find yourself in low orbit. Good job!
Unfortunately, there isn't much time to celebrate.
You happened to be arriving on Earth during an international festival, where
spacecrafts are launched into low orbit, which happens to be where you are.
You can attempt to actively avoid the spacecrafts, using lots of fuel, or you can
let the other ships attempt to dodge YOU, which has a chance of ending your journey
early.


1 - Actively avoid the spacecrafts | 2 - YOU ONLY LIVE ONCE!!!!!!
-2 Fuel Gauge Slots                | 20% chance for survival
(100% certainty)                   | 80% chance for a journey-ending collision
                          What's your choice?
                                   """
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
        print(f"{intro}\n\nA Choose Your Own Adventure game, where you dodge space objects or tightly manage your fuel to reach planet Earth before it runs out or you collide with space junk.\nHighly recommended to have your terminal window maximized.\nPress Enter to begin. ", end="")
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
        try:
            userInput = inputimeout(prompt="", timeout=timer)
            if userInput == sequence:
                print("Nice! You dodged the space junk!")
                time.sleep(1)
                return True
            else:
                continue
        except TimeoutOccurred:
            print(gameOver)
            exit()
        
def pathAround(stage, gauge):
    #procrastination is the devil's incarnation in all humans. (aka this took forever for me to get to)
    #basically is only used for printing statements, all the logic is in the pathAround() part in the main() function.
    time.sleep(1)
    returnValue = ""
    if gauge == 3:
        print(fuelGauge3)
    if gauge == 2:
        print(fuelGauge2)
    if gauge == 1:
        print(fuelGauge1)
    if gauge == 0:
        print(fuelGauge0)
    if stage == 1:
        returnValue = input(stage1Text)
    if stage == 2:
        returnValue = input(stage2Text)
    if stage == 3:
        returnValue = input(stage3Text)
    return returnValue

def main():
    gauge = 3
    #where the magic happens, and my if increases by about 30
    #asks the user for a choice between two paths, and commences the path. Each path has 3 decisions/inputs, and if all 3 are done within tolerance, gameWon screen is shown. else, gameOver is shown.
    if intro() == True:
        choice1 = input(f"{spaceFrame1}\n{spaceText1}")
        while choice1 != 1 or choice1 != 2:
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
                            print(f"{gameWon}\nYou avoided all of the debris, and no major damage was dealt to your ship. Fine work.")
                            break
            elif choice1 == "1":
                print("\nYou have chosen to fly around Earth. However, your ship's treasurer has miscalculated the amount of fuel you have left, and \nwithout some drastic measures, you won't be able to make it to Earth in time. Get ready to make some difficult choices.")
                time.sleep(4)
                #first stage
                choice = pathAround(1, gauge)
                if choice == "1":
                    gauge -= 1
                elif choice == "2":
                    if random.random() >= .50:
                        gauge -= 2
                #second stage
                choice = pathAround(2, gauge)
                if choice == "1":
                    if random.random() >= .60:
                        print(gameOver)
                        break
                if choice == "2":
                    gauge -= 1
                #final stage
                choice = pathAround(3, gauge)
                if choice == "1":
                    gauge -= 2
                if choice == "2":
                    if random.random() <= .20:
                        print(gameOver)
                        break
                #check for gauge
                if gauge < 0:
                    print(gameOver)
                    break
                if gauge >= 0:
                    print(f"{gameWon}\nYou made it back to Earth with enough fuel remaining. Fine work.")
                    break

                    
        else:
            print("Try again.")
    
main()

#some ascii art has been sourced from https://www.asciiart.eu/space/
