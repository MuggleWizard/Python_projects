def main():
    print("")
    print("Welcome to the Email Slicer! ")
    print("")

    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension + "\n")


while True:
    main()
    choose = input("Would you like to continue Y/N:  ")
    if choose == "yes" or choose == "Yes" or choose == "y" or choose == "Y":
        continue
    elif choose == "no" or choose == "No" or choose == "n" or choose == "N":
        print("Goodbye! \n")
        break
