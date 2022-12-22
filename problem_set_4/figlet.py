import random
import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    s = input("Input: ")
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
    print(f"Output: \n{figlet.renderText(s)}")
elif (
    len(sys.argv) == 3
    and sys.argv[2] in figlet.getFonts()
    and sys.argv[1] == ("-f" or "--font")
):
    s = input("Input: ")
    f = sys.argv[2]
    figlet.setFont(font=f)
    print(f"Output: \n{figlet.renderText(s)}")
else:
    sys.exit("Invalid usage")
