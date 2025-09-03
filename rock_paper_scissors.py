import random


while True:

    def play():

        user = input(
            "\nWhat's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        user = user.lower()

        if user not in ['r', 'p', 's']:
            print("Not a valid entry")
            return "ah ah ahhhhhh thats a no no you selected {}".format(user)
        # else:
        #     print("You threw {}.".format(user))

        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            return "You and the computer have chosen {}. It's a tie. ".format(computer)

# r > s, s > p, p > r
        if is_win(user, computer):
            return "You have chosen {} and the computer has chosen {}. You won!\n".format(
                user, computer)
        return "You have chosen {} and the computer has chosen {}. You lost :(\n".format(
            user, computer)

    def is_win(player, opponent):
        # return true if the player beats the opponent
        # winning conditions: r > s , s > p , p > r
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
            return True
        return False

    # restart_game = input("Play again? Yes or No: ").lower()
    # if restart_game == "no" or restart_game == "No" or restart_game == "n":
    #     #!= "n"
    #     print("Farewell valiant fighter!")
    #     break

    print(play())
# print(restart_game())


# def restart_game():

# def restart_game():
#     player_input = input("\n Play again? Yes or No "). lower()
#     if player_input == "no" or player_input == "No" or player_input == "n":
#         print("byeeeee")
#         break
#     elif player_input == "yes" or player_input == "Yes" or player_input == "y":
#         print("Here we go!")

# if__name__ == '__rock_paper_scissors__':
#     print(play())
