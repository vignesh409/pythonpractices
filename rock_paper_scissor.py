# from optparse import Option
import random
# from ssl import Options

user_wins=0
comp_wins=0


options=["rock","paper","scissors"]
# Options[0]="rock"
# Options[1]="rock"
# Options[2]="rock"



while True:
    user_input=input("Type Rock/Paper/scissors or Q to quit ").lower()
    if user_input=="q":
        break

    if user_input not in options :
        continue

    random_number=random.randint(0,2)
    #rock:0,paper:1,scissor:2

    computer_pick=options[random_number]
    print("Computer Picked:"+computer_pick)


    if user_input=="rock" and computer_pick=="scissors":
        print("You Win")
        user_wins+=1
        continue
    elif user_input=="paper" and computer_pick=="rock":
        print("You Win")
        user_wins+=1
        continue
    elif user_input=="scissors" and computer_pick=="paper":
        print("You Win")
        user_wins+=1
        continue

    else:
        print("You Lost")
        comp_wins+=1

print("Bye!!")