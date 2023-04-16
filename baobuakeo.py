from random import randint

print("Nhap Bua, Keo, La: ")
player = input()
computer = randint(0,2)

if computer == 0:
    computer = "Bua"
if computer == 1:
    computer = "Keo"
if computer == 2:
    computer = "La"

print("-----")
print("You choose: " + player)
print("Computer choose: " + computer)
print("-----")

if player == computer:
    print("Draw")
else:
    if player == "Bua":
        if computer == "Keo":
            print("Win")
        else:
            print("Lose")

    elif player == "Keo":
        if computer == "Bua":
            print("Lose")
        else:
            print("Win")

    elif player == "La":
        if computer == "Bua":
            print("Lose")
        else:
            print("Win")
    else:
        print("Nhap sai!")