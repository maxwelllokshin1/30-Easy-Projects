import random

num = random.randint(1, 100)
numOfGuesses = 0

while True:
    numOfGuesses += 1
    user = int(input("Enter number 1 - 100: "))
    if user == num:
        break
    elif user > num:
        print("Lower")
    else:
        print("Higher")

print("Correct!! it took", numOfGuesses, "many of guesses")