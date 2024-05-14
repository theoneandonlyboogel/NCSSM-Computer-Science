#pyfiglet functions are commented out because of trinket dependencies being limited.
import random
import string
#import pyfiglet

#adjective list
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
    "unacceptable",
    "adamant",
    "endemic",
    "friable",
    "gustatory",
    "incendiary",
    "judicious",
    "meretricious",
    "recalcitrant"

]
#noun list
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
    "macroeconomics",
    "performance",
    "discussion",
    "sympathy",
    "independence",
    "replacement",
    "poetry"
]

#vars to avoid using pyfiglet, which is incompatible with Trinket used to submit
passwordPicker = """
 ______                                           __ 
|   __ \.---.-.-----.-----.--.--.--.-----.----.--|  |
|    __/|  _  |__ --|__ --|  |  |  |  _  |   _|  _  |
|___|   |___._|_____|_____|________|_____|__| |_____|
                                                     
 ______ __        __               
|   __ \__|.----.|  |--.-----.----.
|    __/  ||  __||    <|  -__|   _|
|___|  |__||____||__|__|_____|__|  
                                   """

cya = """
 ______               __ 
|      |.--.--.---.-.|  |
|   ---||  |  |  _  ||__|
|______||___  |___._||__|
        |_____|          
"""

#print(pyfiglet.figlet_format("Password Picker",font= "chunky"))
print(passwordPicker) #intro sequence
#begins main while loop
while True:
    #asks how many passwords
    qty = int(input("How many passwords? "))
    #goes until i == qty
    for i in range(0, qty):
        #determining password element vars, basically each segment of the password
        adjective = random.choice(adjectives)
        noun = random.choice(nouns)
        number = random.randrange(0, 100000)
        specialChar = random.choice(string.punctuation)

        adjNoun = adjective + "_" + noun
        #used for defining a order for the different words and characters,
        #creates a list with random digits, always 3 entries long
        #if num generated is already there, ignore and keep going, go until list is 3 long
        order = []
        while len(order) < 3:
            t = random.randint(1, 3)
            if t not in order:
               order.append(t)
               i+1
            else:
               continue
            #formation of the full string, with all the digits, 1 2 or 3. (.replace is just formatting)
            fullString = "".join(str(order)).replace("[", "").replace("]", "").replace(",", "")
        #replacement with actual password elements, printing of the password
        password = str(fullString.replace("2", adjNoun).replace("1", specialChar).replace("3", str(number)).replace(" ", ""))
        print(password)
        i += 1
    #then asks for regeneration of said passwords
    userInput = input("Would you like more passwords? Type Y/n ").lower()
    if userInput == "n":
        #print(pyfiglet.figlet_format("Cya!",font= "chunky"))
        print(cya)
        break
    if userInput == "y":
        continue
