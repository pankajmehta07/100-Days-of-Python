import random

total_cash = 5000
print("\n\n\t\t\tCho-Han\n")

print("In this traditional Japanese dice game, two dice are rolled in a bamboo cup by the dealer sitting on the floor. The player must guess if the dice total to an even (cho) or odd (han) number.")

bet = input(f"\nYou have {total_cash} mon. How much do you bet? (or QUIT):\t")
if bet.lower()!="quit" and bet.isnumeric():
    bet = int(bet)
    if bet<total_cash:
        print("The dealer swirls the cup and you hear the rattle of dice. The dealer slams the cup on the floor, still covering the dice and asks for your bet.")
        guess = input("\nCHO (even) or HAN (odd):\t")
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        dice = "cho" if (dice1+dice2)%2==0 else "han"
        print(f"GO - GO")
        print(dice)
        print(f"\n{dice1} - {dice2}")
        if guess.lower()==dice:
            print(f"You won! You take {bet*2} mon.")
            print(f"\nThe house collects {int(bet*0.05)} mon fee.")
        else:
            print(f"You lost {bet} mon")
    else:
        print("You should bet less than your total money.")








