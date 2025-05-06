# rock > scissors
# Scissors > Paper
# Paper > Rock

import random
import time

def winOrLose(comp, option):
    if comp == winners[option]: # user won
        return 1
    elif option == winners[comp]: # computer won
        return 2
    return 0

options = (
    "rock",
    "paper",
    "scissors",
)

winners = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

while True:
    print("==========================")
    print("Rock > Scissors" \
        "\nPaper > Rock" \
        "\nScissors > Paper")
    print("==========================")
    time.sleep(2)
    user = input("Choice -" \
                    "\n -Rock" \
                    "\n -Paper" \
                    "\n -Scissors" \
                    "\n -Exit" \
                    "\n CHOSEN: ")
    comp = options[random.randint(0,2)]

    if user.lower() == "exit":
        break

    if user.lower() in options:
        print("-------------------")
        if winOrLose(comp.lower(), user.lower()) == 1:
            print("YOU WON -", user.lower(), ">", comp.lower())
        elif winOrLose(comp.lower(), user.lower()) == 2:
            print("you lose -", user.lower(), "<", comp.lower())
        else:
            print("Draw -", user.lower(), "=", comp.lower())
        print("-------------------")
        time.sleep(2)
    else:
        print("INVALID")
        time.sleep(2)