import random

input("Press Enter to start the game")

min = 1
max = 100

print(f"I've chosen a number between {min} and {max}")

toGuess = random.randint(min, max)

print(f"First digit is {str(toGuess)[0]}")

chosen = input("Enter a number ")

#toGuess != chosenn doesn't work
while(str(toGuess) != chosen):  # input returns a string, so we need to cast toGuess to a string to correctly compare to chosen
    print("You're wrong. Try again!")
    chosen = input("Enter a number ")

print("Got it!")
