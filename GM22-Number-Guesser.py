import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a good number larger than 0')
        quit()
else:
    print('Please type a number')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

print(random_number)

while True:
    guesses += 1
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number')
        quit()
    if user_guess == random_number:
        print("Awesome youre a genius!")
        break
    else:
        print("you got it wrong! LOSER!")

print("you got it in", guesses, "guesses")