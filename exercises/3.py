import random as rnd

random_number = rnd.randint(0,100)

guess_input = int(input("Type your guess:\t"))

while guess_input != random_number:
    if random_number > guess_input:
        guess_input = int(input("Increase your number:\t"))
    else:
        guess_input = int(input("Decrease your number:\t"))

print("You found the correct number:\t" + str(guess_input))