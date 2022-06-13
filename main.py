import random

while True:
    choices = ["r","p","s"]

    CPU = random.choice(choices)
    player = input("r, p, or s?: ").lower()

    while player not in choices:
        player = input("ERROR! r, p, or s?: ").lower()

    if player == CPU:
        print("player: ",player,end=", ")
        print("CPU: ",CPU)
        print("Tie!")

    elif player == "r":
        if CPU == "p":
            print("player: ",player,end=", ")
            print("CPU: ",CPU)
            print("You lose!")
        if CPU == "s":
            print("player: ",player,end=", ")
            print("CPU: ",CPU)
            print("You win!")
            break

    elif player == "s":
        if CPU == "r":
            print("player: ",player,end=", ")
            print("CPU: ",CPU)
            print("You lose!")
        if CPU == "p":
            print("player: ",player,end=", ")
            print("CPU: ",CPU)
            print("You win!")
            break

    elif player == "p":
        if CPU == "s":
            print("player: ",player,end=", ")
            print("CPU: ",CPU)
            print("You lose!")
        if CPU == "r":
            print("player: ",player,end=", ")
            print("CPU: ",CPU)
            print("You win!")
            break

    play_again = input("Wanna play again? (y/n): ").lower()

    if play_again != "y":
        break

print("Bye!")