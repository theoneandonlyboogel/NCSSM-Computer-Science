from pyfiglet import Figlet
import sys
from random import choice

figlet = Figlet()
fontList = figlet.getFonts()

if len(sys.argv) == 1:
    randFont = choice(fontList)
    figlet.setFont(font=randFont)

elif len(sys.argv) == 3:
    specificFont = sys.argv[2]
    if sys.argv[1] == "-f" or sys.argv[1] == "--font" and specificFont in fontList:
        figlet.setFont(font=specificFont)
    else:
        sys.exit("Invalid usage")
else:
    exit("Invalid usage")

figText = input("Input: ")
print("Output:", figlet.renderText(figText), sep="\n")
