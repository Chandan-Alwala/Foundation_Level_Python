#guess the pre-defined secret number
turns = 3
secret = 5
i = 0
while (i < turns):
    guess = int(input("Your guess: "))
    i = i +1
    if (guess != secret and i != turns):
        print("Try again")
    elif (guess != secret and i == turns):
        print("Failed")
    elif (guess == secret ):
        print("Success")
        break

