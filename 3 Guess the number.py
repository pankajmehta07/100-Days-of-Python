import numpy as np

print("I'm thinking of a number between 1 and 100, try to guess it")

play = True
while play:

    choose = True
    while choose:
        diff = input("Choose a difficulty. Type 'easy' | 'medium' | 'hard':\t")
        choose = False
        if diff == "easy":
            guesses = 10
        elif diff == "medium":
            guesses = 6
        elif diff == "hard":
            guesses =3

        else:
            print("You have to choose from easy | medium | hard.\n Please try again!!\n")
            choose = True

    imagined = np.random.randint(1,100)

    guess = False
    correct = False
    while not guess and guesses >0:
        print("You have {} guesses left for the number that I'm thinking of.".format(guesses))
        user = int(input("Take your guess:\t"))
        guesses -= 1

        if imagined==user:
            print("\nCorrect! The answer was {}. Thanks for completing that!\n".format(user))
            correct = True
            break

        elif imagined-user>0:
            print("Too Low")

        else:
            print("Too High")

    if not correct:
        print("\n\t\t\tYou Lost!!!. \n The answer was {}. Better luck next time!\n".format(imagined))

    again = input("\nDo you want to play again? Type 'y' if yes and 'n' to quit:\t" )
    if again.lower()!='y':
        play = False
        print("Thank You!")





