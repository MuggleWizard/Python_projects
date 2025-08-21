import random

high_score = 0


def dice_game():
    global high_score
    while True:
        print("Current High Score: ", high_score, "\n")
        print("1) Roll Dice")
        print("2) Leave Game \n")
        choice = int(input("Enter you choice: "))
        if choice == 2:
            print("Goodbye! \n")
            quit()
        pips1 = random.randint(1, 6)
        pips2 = random.randint(1, 6)
        print("")
        print("You roll a...", pips1)
        print("You roll a...", pips2, "\n")
        total_dice = pips1 + pips2
        print("You have rolled a total of:", total_dice, "\n")
        print("New high score!\n")

        if total_dice > high_score:
            high_score = total_dice
            print("Current High Score", total_dice, "\n")
            if total_dice == 12:
                print("You are the ultimate player! \n")
                break
        else:
            print("Don't stop believing! \n")


dice_game()
