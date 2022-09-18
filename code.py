import random
while True:
    print("enter your choice\n 1.Rock\n 2.Paper\n 3.scissors\n")
    choice = int(input("User turn:"))
    while choice > 3 or choice < 1:
        choice = int(input("enter valid option"))
    if choice == 1:
        choice_name = "ROCK"
    elif choice == 2:
        choice_name = "PAPER"
    else:
        choice_name = "SCISSORS"
    print("User choice is: "+choice_name)
    print("\n Now it's computer turn..")
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = "ROCK"
    elif comp_choice == 2:
        comp_choice_name = "PAPER"
    else:
        comp_choice_name = "SCISSORS"
    print("Computer choice is:"+comp_choice_name)
    print(choice_name + "V/S" + comp_choice_name)
    if (choice == 1 and comp_choice == 1) or (choice == 2 and comp_choice == 2) or (choice == 3 and comp_choice == 3):
        print("TIE", end="")
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        print("PAPER wins", end="")
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print("ROCK wins", end="")
    else:
        print("SCISSOR wins", end="")
    print("\nDo you wanna play again?(Y/N)")
    ans = input()
    if ans == 'n' or ans == 'N':
        print("\nThanks for playing")
        break
