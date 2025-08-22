import random

high_score = 0
counter = 0


def dice_game():
    global high_score
    global counter
    while True:
        print("\n Current High Score: ", high_score, "\n")
        print("\n Current counter value:", counter, "\n")
        print()
        print("1) Roll Dice")
        print("2) Leave Game \n")
        choice = int(input("Enter you choice: "))
        if choice == 1:
            counter += 1
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
        if counter >= 10:
            print("Counter has reached the limit! Better luck next time!")
            break

        if total_dice > high_score:
            high_score = total_dice
            print("Current High Score", total_dice, "\n")
            print("New high score! \n")
        if total_dice < high_score:
            print("Bananas! ")
            print("Suns of the pharaoh! ")
        if total_dice == 12:
            print("You are the ultimate player! \n")
            break
        else:
            print("Keep trying! \n")


dice_game()

# if total_dice < high_score:
#     high_score = total_dice
#     print("Keep trying! \n")
# elif total_dice > high_score:
#     high_score = total_dice
#     print('New high score! \n')

# SuperBeastArt!  RASENGAN!!!!
# Chidori!!!
