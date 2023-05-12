import numpy as np

def winner(inp1,inp2):
    if inp1 == "Rock" and inp2=="Paper" or inp2 == "Rock" and inp1=="Paper":
        return "Paper"
    elif inp1 == "Rock" and inp2=="Scissors" or inp2 == "Rock" and inp1=="Scissors":
        return "Rock"
    if inp1 == "Scissors" and inp2=="Paper" or inp2 == "Scissors" and inp1=="Paper":
        return "Scissors"



options = {0:'Rock',1:'Paper',2:'Scissors'}

print("\n\n\n\tWelcome to the ROCK PAPER SCISSORS Game!\n\n")
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
computer = np.random.randint(0,2)

print("You choose: {}".format(options[user]))
print("The Computer choose: {}".format(options[computer]))


if user == computer:
    print("Tied!! Both entered the {}".format(options[user]))
else:
    win = winner(options[user],options[computer])

    if win == options[user]:
        print("You won !!. {} wins against {}".format(options[user],options[computer]))
    else:
        print("You Lost !!. {} wins against {}".format(options[computer],options[user]))


