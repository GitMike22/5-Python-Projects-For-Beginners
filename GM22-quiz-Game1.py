print("Welcome idiot!")

playing = input("Do you want to play a game? ")

if playing != "yes":
    quit()

print("okay! Lets play! :)")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does USMC stand for? ")
if answer.lower() == "united states marine corps":
    print('correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does NAVY stand for? ")
if answer == "never again volunteer yourself":
    print('correct!')
    score += 1
else:
    print('Incorrect!')

print("You got " + str(score) + " questions correct!")
print("You got " + str((score) / 3)*100 + "%!" )
