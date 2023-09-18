import random


print("")
pips = random.randint(1, 6)
print("You roll the die... it lands with", pips, "pips showing. \n")

prizes = ["a car", "$100000", "a pony", "$500000", "a castle"]
prize_won = random.choice(prizes)
print("You turn the wheel of fortune... It lands on a prize of", prize_won + "!! \n")

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
random.shuffle(cards)
print("The cards are now in this order: ")
print(cards, "\n")
