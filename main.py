BANNER = r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''


def intro():
    """Displays the welcome banner and introduction text."""
    print(BANNER)
    print("Welcome to the Lost Treasure Island! 🏝️\n")
    print("You are a brave explorer who discovered an ancient map.")
    print("The treasure is hidden somewhere on the island...")
    print("Good luck on your adventure!\n")
    print("You arrive at a fork in the jungle path.")
    print("To the LEFT, you see a narrow path covered with vines and exotic flowers.")
    print("To the RIGHT, there's a wide path with recent footprints on the ground.\n")


def choose_door():
    """
    Handles the final cave decision (door choice).
    Returns True if the player wins, False otherwise.
    """
    print("\nYou enter the dark cave. In front of you are three mysterious doors:")
    print("🔴 RED Door    — Glows intensely with flame drawings")
    print("🟡 YELLOW Door — Has gold symbols engraved")
    print("🔵 BLUE Door   — Drips water and you hear a river\n")

    path_3 = input("Which door do you choose? (red / yellow / blue)\n> ").strip().lower()

    if path_3 == "red":
        print("\nDEATH 🔥")
        print("You opened the door and were consumed by fire! ❌ GAME OVER! ❌")
        return False
    elif path_3 == "blue":
        print("\nDEATH 🌊")
        print("You opened the door and were swept away by a flood! ❌ GAME OVER! ❌")
        return False
    elif path_3 == "yellow":
        print("\nVICTORY 🏆")
        print("You opened the yellow door and found the treasure! 💰💎👑 Congratulations, you win!")
        return True
    else:
        print("\nInvalid choice. The cave rumbles and collapses... ❌ GAME OVER! ❌")
        return False


def cross_lake():
    """
    Handles the lake crossing decision.
    Returns True if the player survives, False otherwise.
    """
    print("\n--- Lake with Island ---")
    print("After hours of walking, you reach a crystal-clear lake.")
    print("In the middle of the lake, you see a small island with a mysterious cave.\n")
    print("SWIM — Cross the lake yourself.")
    print("WAIT — Wait for help.")
    print("BOAT — Look for a boat nearby.\n")

    path_2 = input("Will you cross? (swim / wait / boat)\n> ").strip().lower()

    if path_2 == "wait":
        print("\nYou waited patiently. A mysterious boatman appeared and took you safely to the island! ✅")
        return True
    elif path_2 == "swim":
        print("\nYou started swimming but piranhas attacked you! ❌ GAME OVER! ❌")
        return False
    elif path_2 == "boat":
        print("\nWhile you were looking for a boat, a giant crocodile got you! ❌ GAME OVER! ❌")
        return False
    else:
        print("\nInvalid choice. Hesitating too long, quicksand swallowed you... ❌ GAME OVER! ❌")
        return False


def treasure_hunt():
    """
    Main game function. Guides the player through the three
    decision points of the treasure hunt adventure.
    """
    intro()

    path_1 = input("Choose your path. Narrow path turn LEFT. Wide path turn RIGHT.\n> ").strip().lower()

    if path_1 == "left":
        print("\nYou continue safely! ✅")
        if not cross_lake():
            return
        if not choose_door():
            return

    elif path_1 == "right":
        print("\nYou followed the footprints and were attacked by wild monkeys! ❌ GAME OVER! ❌")

    else:
        print("\nInvalid choice. You wandered into the jungle and got lost... ❌ GAME OVER! ❌")


if __name__ == "__main__":
    treasure_hunt()
    print("\nThank you for playing!")
