# Input:
#
# Take input n, mn, and mx from the user.
#
# Output:
# Print whether the numbers between mn and mx are divisors of “n” or not.
# If mn=mx, show that this is not a range, and mn is equal to mx. Show the result for that number.
#
# Example:
# If n is 20 and mn=2 and mx=5
#
# 2 is a divisor of20
#
# 3 is not a divisor of 20
#
# …
#
# 5 is a divisor of 20
while True:
    try:
        apple = int(input("Enter the number of apples: "))
        mn = int(input("Enter the minimum number of range: "))
        mx = int(input("Enter the maximum number of range: "))

    except ValueError:
        print("Only integers are allowed!!")
        exit()
    if mn == mx:
        print("It is not in an Range!!")
        if apple % mn == 0:
            print(f"{mn} is a divisor of {apple}")
        else:
            print(f"{mn} is not a divisor of {apple}")
    elif mn > mx:
        print("The minimum can't be Greater number!!")

    else:
        for i in range(mn, mx + 1):
            if apple % i == 0:
                print(f"{i} is a divisor of {apple}")
            else:
                print(f"{i} is not a divisor of {apple}")
    choice = ""
    while choice != "q" and choice != "c":
        choice = input("Enter 'q' to quit OR 'c' to continue: ").isupper()
        if choice == 'q':
            exit()
        elif choice == "c":
            continue