print("\n\n\n\tWelcome to the tip calculator!\n\n")
print("What is the total bill amount?")
bill = float(input("Bill Amount :\t"))
print("How much tip would you like to give?")
tip = float(input("Percent : \t"))
print('How many people to split the bill?')
people = float(input("People :\t"))

print("\n\nEach person should pay {}".format(bill*(100+tip)/(100*people)))



