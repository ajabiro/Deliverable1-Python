name = input("Welcome to GC golf! What is your name?")
number_of_holes = int(input("Hi " + name + "! " "Would you like to play 3 or 6 holes?"))

if number_of_holes == 3:

    hole1 = int(input("How many putts for hole 1? (par: 3)"))
    hole2 = int(input("How many putts for hole 2? (par: 3)"))
    hole3 = int(input("How many putts for hole 3? (par: 3)"))

    score = int(hole1 + hole2 + hole3 - 9)

    if score > 9:
        print(f"Nice try {name}... Your total score was: {score}")
    elif score < 9 & score > 0:
        print(f"Great job, {name}! Your total score was: {score}")
    else:
        print(f"Good game, {name}. Your total score was: {score}")

else:
    hole1 = int(input("How many putts for hole 1? (par: 3)"))
    hole2 = int(input("How many putts for hole 2? (par: 3)"))
    hole3 = int(input("How many putts for hole 3? (par: 3)"))
    hole4 = int(input("How many putts for hole 4? (par: 3)"))
    hole5 = int(input("How many putts for hole 5? (par: 3)"))
    hole6 = int(input("How many putts for hole 6? (par: 3)"))
    score = int(hole1 + hole2 + hole3 + hole4 + hole5 + hole6 - 18)

    if score > 18:
        print(f"Nice try {name}... Your total score was: {score}")
    elif score < 18 & score > 0:
        print(f"Great job, {name}! Your total score was: {score}")
    else:
        print(f"Good game, {name}. Your total score was: {score}")