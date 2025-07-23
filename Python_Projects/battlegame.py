while True:
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    orc = "Orc"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 175

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 125

    dragon_hp = 300
    dragon_damage = 50

    while True:
        print("1. Wizard")
        print("2. Elf")
        print("3. Human")
        print("4. Orc")
        option = input("Choose your character: ").lower()
        if option == "1" or option == "Wizard" or option == "wizard":
            print("Wizard")
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif option == "2" or option == "Elf" or option == "elf":
            print("Elf")
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif option == "3" or option == "Human" or option == "human":
            print("Human")
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif option == "4" or option == "Orc" or option == "orc":
            print("Orc")
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        else:
            # print("Invalid command")
            print("Unknown character")

    print("You have chosen the character: " + character)
    print("Health: ", my_hp)
    print("Damage: ", my_damage)
    print()

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The", character, "damaged the Dragon!")
        print("The Dragon's hitpoints are now: ", dragon_hp)
        print()

        if dragon_hp > 0:
            print("The Dragon strikes back at", character)

        if dragon_hp <= 0:
            print("The Dragon has lost the battle. \n ")
            break

        my_hp = my_hp - dragon_damage
        print("The", character, "hitpoints are now: ", my_hp)
        print()

        if my_hp <= 0:
            print("The", character, "has lost the battle. \n ")
            break

    restart_game = input("Battle again? Yes or No: ").lower()
    if restart_game == "no" or restart_game == "No" or restart_game == "n":
        #!= "n"
        print("Farewell valiant fighter!")
        break
