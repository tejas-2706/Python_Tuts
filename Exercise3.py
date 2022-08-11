# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over

n=18
number_of_guesses=1
print("guesses of no. is limited to 9:")
while(number_of_guesses<=9):
    guess_number= int(input("guess the number:"))
    if guess_number>18:
        print("guess no. is greater")
    elif guess_number<18:
        print("guess no. is less")
    else :
        print("you won the game")
        print(number_of_guesses,"no. of guesses needed")
        break
    print(9-number_of_guesses,"left guesses are:")
    number_of_guesses = number_of_guesses + 1

if(number_of_guesses>9):
    print("GAME OVER")