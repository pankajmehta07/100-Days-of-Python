import numpy as np
print("\n\t\tBagels, a deductive logic game.\n\n")

print("I am thinking of a 3-digit number. Try to guess what it is.\nHere are some clues:\nWhen I say:")
print("Pico --> One digit is correct but in the wrong position.\nFermi --> One digit is correct and in the right position.\nBagels --> No digit is correct.")
print("I have thought up a number.\nYou have 10 guesses to get it.\n")
run = True
while run:
    imagined_num = str(np.random.randint(100,1000))
    win = False
    for i in range(10):
        guess = input("\nGuess #{}\t".format(str(i+1)))
        if len(guess)==3:
            if guess == imagined_num:
                print("You got it!")
                win = True
                break
            else:
                count = 0
                for i in range(3):
                    if guess[i] in imagined_num:
                        count+=1
                        if guess[i]==imagined_num[i]:
                            print("Fermi",end=" ")
                        else:
                            print("Pico",end=" ")
                if count==0:
                    print("Bagels")
        else:
            print("Only 3 digit numbers are allowed")
    if not win:
        print("\n\tYou Lost!!\n")
    if input("Do you want to play again? (yes or no)\t").lower()!="yes":
        run=False
        print("\tThanks for playling!!")


