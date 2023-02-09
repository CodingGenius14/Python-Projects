import random

guessesTaken = 0

name = input("Hi, what is your name? ")

number = random.randint(1, 10)

print()

print(f"Hi {name}, I am thinking of a number between 1 and 10, it is your job to guess this number! You have 3 guesses.")

print()

for i in range(3):
    guessesTaken += 1
    guess = int(input("Take a guess: "))

    if guess > number:
        print("Your guess was too high")
    elif guess < number:
        print("Your guess was too low")
    elif guess == number:
        break

if guess == number:
    print(f"Congratulations {name}, you guessed correctly in {guessesTaken} guesses")

if guess != number:
    print(f"Sorry, that is not correct. The number I was thinking of was {number}")


