favorite_number = 8
attempts = range(3)
for attempts in attempts:
    guess = int(input("Please enter a favorite number: \n"))
    if guess == favorite_number:
        print("you win, game over")
        break
    else:
        print ("Try Again")
