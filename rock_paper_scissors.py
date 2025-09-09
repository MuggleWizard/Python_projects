import random

games_played = 0

while True:

    def play():
        print("")
        print(f"Game {games_played + 1}")

        user = input(
            "\nWhat's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
        user = user.lower()

        if user == 'r':
            print("""
                     _________
            ________|.   _____)
                     __(_______)
                    (__________)
            _________(_________)
                    |__(_______)
            """)

        if user == 'p':
            print("""
                  ________
            ______|. _____)___
                       _______)_
                      __________)
              __        ________)
                |______________)
                      
             """)

        if user == 's':
            print("""
            _________     
        ____|    ____)_____
                    _______)
                  __________)
            ___    (_____)
               |__(____)
                  
                  """)

        if user not in ['r', 'p', 's']:
            print("Not a valid entry")
            return "ah ah ahhhhhh thats a no no you selected {}".format(user)

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

    print(play())

    restart_game = input("\nPlay again? Yes or No: ").lower()

    match restart_game:
        case "no" | "n" | "No":
            print("Adios senor")
            break
        case "yes" | "y" | "Yes":
            print("As you wish")
            games_played += 1
            print(f"Total rounds played: {games_played}")
        case _:
            print("That's not a valid response amigo")

    # If statement code that works as well.  Updated to switch case code above for cleaner and more readible code.
    # if restart_game == "no" or restart_game == "No" or restart_game == "n":
    #     #!= "n"
    #     print("\nFarewell valiant fighter!\n")
    #     break
    # elif restart_game == "yes" or restart_game == "y" or restart_game == "Yes":
    #     print("Game on!")
    # else:
    #     print("That's not a valid response you donkey")


# if__name__ == '__rock_paper_scissors__':
#     print(play())

        # if counter >= 10:
        #     print("Counter has reached the limit! Better luck next time! \n")
        #     break
