import random as rd

top_range = input("Enter the Range Number: ")

if top_range.isdigit():
    top_range = int(top_range)

    if top_range <= 0:
        print("Please Enter Larger Number!")
else:
    print("Please Enter Number!")

random_Number = rd.randint(0, top_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Enter the Gusses Number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please Enter the Number Next Time!")
        continue

    if user_guess == random_Number:
        print("You Got It $$$")
        break
    elif user_guess > random_Number:
        print("Your Number is Above the Number!")
    else:
        print("Your Number is Below the Number!")

print("You guess it in", guesses)



