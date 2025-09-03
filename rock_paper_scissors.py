import random


def play():

    while True:
        user = input(
            "What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        user = user.lower()

        if user not in ['r', 'p', 's']:
            print("Not a valid entry")
            continue
        else:
            print("You threw {}.".format(user))

        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            print("You and the computer have chosen {}. It's a tie. ").format(
                computer)

    # r > s, s > p, p > r
        if is_win(user, computer):
            return "You have chosen {} and the computer has chosen {}. You won!".format(user, computer)
        return "You have chosen {} and the computer has chosen {}. You lost :(".format(user, computer)


def restart_game():
    player_input = input("\n Play again? Yes or No "). lower()
    if player_input == "no" or player_input == "No" or player_input == "n":
        print("byeeeee")
    elif player_input == "yes" or player_input == "Yes" or player_input == "y":
        print("Here we go!")


def is_win(player, opponent):
    # return true if the player beats the opponent
    # winning conditions: r > s , s > p , p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False


print(play())
print(restart_game())


# def restart_game():

#     restart_game = input("Battle again? Yes or No: ").lower()
#     if restart_game == "no" or restart_game == "No" or restart_game == "n":
#         #!= "n"
#         print("Farewell valiant fighter!")
#         # break
