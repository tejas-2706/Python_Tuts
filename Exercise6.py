# rock,paper,scissors game using random variable
# by while loop should run for 10 times and at
# last declare the winner

import emojis
print(emojis.encode("\t \t \t \t :india::heart: :fist: :raised_hand_with_fingers_splayed: :scissors: :india::heart:"))
print("\t \t \t \t TOTAL CHANCES ARE: 10 ")
import random
my_points=0
computer_points=0
#player_input = input(("Enter your choice betweew [rock,paper & scissors]:"))
number_of_guesses=0
while (number_of_guesses<10):
    player_input = input(("Enter your choice betweew [rock,paper & scissors]:"))
    if player_input == "rock":
        lst = ["Rock", "Paper", "scissors"]
        choice_lst = random.choice(lst)
        print(choice_lst)
        if choice_lst == "Rock":
            print("TIE")
            print("No points")
        elif choice_lst == "Paper":
            print("winner is paper!!")
            computer_points = computer_points+1
            print("computer_points is:" , computer_points)
        elif choice_lst == "scissors":
            print("winner is rock [You Win!!]")
            my_points = my_points+1
            print("my_points is:" , my_points)
        else:
            print("error")
    elif player_input == "paper":
        lst = ["Rock", "Paper", "scissors"]
        choice_lst = random.choice(lst)
        print(choice_lst)
        if choice_lst == "Rock":
            print("winner is paper [You Win!!]")
            my_points = my_points + 1
            print("my_points is:", my_points)
        elif choice_lst == "Paper":
            print("TIE")
            print("No points")
        elif choice_lst == "scissors":
            print("winner is scissors!!")
            computer_points = computer_points + 1
            print("computer_points is:", computer_points)
        else:
            print("error")
    elif player_input == "scissors":
        lst = ["Rock", "Paper", "scissors"]
        choice_lst = random.choice(lst)
        print(choice_lst)
        if choice_lst == "Rock":
            print("winner is rock!!")
            computer_points = computer_points + 1
            print("computer_points is:", computer_points)
        elif choice_lst == "Paper":
            print("winner is scissors [You Win!!]")
            my_points = my_points + 1
            print("my_points is:", my_points)
        elif choice_lst == "scissors":
            print("TIE")
            print("No points")
        else:
            print("error")
    else:
        print("error!!")
    number_of_guesses=number_of_guesses+1
    print(f"you have used {number_of_guesses} chance!!")
if ( number_of_guesses > 10):
    print("Total score of my points is:" , my_points)
    print("Total score of computer points is:", computer_points)
    if (my_points>computer_points):
        print(emojis.encode(f"YOU WON THE GAME!!:trophy:"))
    elif (computer_points>my_points):
        print("YOU LOOSE THE GAME!!")
    else:
        print("THE MATCH IS TIE")


print("Game Over!!")








# lst = ["Rock","Paper","Scissors"]
# choice_lst = random.choice(lst)
# print(choice_lst)




# rock paper = winner is paper
# rock scissors = winner is rock
# paper scissors = winner is scissors
# rock rock = paper paper = scissors scissors = TIE match
