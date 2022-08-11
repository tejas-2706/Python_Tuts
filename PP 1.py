# The task you have to perform is “Your Age In 2090”.
# This task consists of a total of 10 points to evaluate your performance.
#
# Problem Statement:-
# Take age or year of birth as an input from the user. Store the input in one variable.
# Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).
#
# Here are a few instructions that you must have to follow:
#
# Do not use any type of module like DateTime or date utils. (-5 points)
# Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
# Your code should handle all sorts of errors like :            (2 points)
# You are not yet born
# You seem to be the oldest person alive
# You can also handle any other errors, if possible!


# age = int(input("What is your age OR Birth of Date?"))
while True:
    age = int(input("What is your age OR Birth of Date? "))
    if 1 <= age <= 100:
        print(f"You will turn 100 years old after {100 - age} Years, b'coz its 2022!!")
    elif 1900 <= age <= 2022:
        b_o_y = 100 - (2022 - age)
        print(f"You will turn 100 years old after {b_o_y} Years, b'coz its 2022!!")
        print(f"The Year will be {age + 100} !!")
    elif 100 < age < 200:
        print("You seem to be the oldest person alive")
    elif 1 > age:
        print("You are not yet born")
    elif 1900 < age < 1800:
        print("You seem to be the oldest person alive")
    elif 2022 < age:
        print("You are not yet born")
    else:
        print("Wrong input !!!")
    interested_year = int(input("Which year you are interested to see your age? "))
    print(f"your age will be {interested_year - age} years at {interested_year} year !!")
    choice = ""
    while choice != "q" and choice != "c":
        choice = input("Enter 'q' to quit OR 'c' to continue !!")
        if choice == "q":
            quit()
        elif choice == "c":
            continue




