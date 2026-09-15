from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
figlet_list = figlet.getFonts()

if len(sys.argv) == 1 or len(sys.argv) == 3:

    if len(sys.argv) == 1:
        txt = input("Input: ")
        f = random.choice(figlet_list)
        figlet.setFont(font=f)
        print(figlet.renderText(txt))

    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            if sys.argv[2] in figlet_list:
                txt = input("Input: ")
                figlet.setFont(font=sys.argv[2])
                print(figlet.renderText(txt))

            else:
                sys.exit("Invalid usage")

        else:
            sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")


