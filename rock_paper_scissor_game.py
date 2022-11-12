import random

choices=["Rock","Paper","Scissor"]

player_choice= str(input("Enter your choice(Rock\Paper\Scissor): "))
computer_choice= random.choice(choices)

print("Player choice is: ",player_choice)
print("Computer choice is: ",computer_choice)

if player_choice == computer_choice:
    print("Match Tied")
elif player_choice=="Rock":
    if computer_choice=="Paper":
        print("Computer Won")
    else:
        print("****** Player won *********")

elif player_choice=="Paper":
    if computer_choice=="Scissor":
        print("Computer Won")
    else:
        print("****** Player won *********")

elif player_choice=="Scissor":
    if computer_choice=="Rock":
        print("Computer Won")
    else:
        print("****** Player won *********")
else: 
    print("Wrong choice...")


