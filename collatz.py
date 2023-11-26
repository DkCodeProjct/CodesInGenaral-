import sys
from pyfiglet import Figlet

figlet = Figlet()
figlet.getFonts()

# if len(sys)>2 gt font name and print \\
if len(sys.argv) > 2:
    figlet.setFont(font=sys.argv[2]) #getFontStylr
    print(figlet.renderText(f">__ {sys.argv[3]} __<")) #printingOutFont with sys.argv[3]
else:
    print("Too Few Arguments>_ _") # if sys<2 Show Error



