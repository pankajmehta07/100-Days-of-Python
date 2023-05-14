import string
import random

print("\n\n\t\tWelcome to the PyPassword Generator!\n\n")
letter = int(input("How many letters would you like in your password?\t"))
symbol = int(input("How many symbols would you like in your password?\t"))
number = int(input("How many numbers would you like in your password?\t"))

random.choice
letters = "".join([random.choice(string.ascii_letters) for i in range(letter)])
numbers = "".join([random.choice(string.digits) for i in range(number)])
symbols = "".join([random.choice(string.punctuation) for i in range(symbol)])
pwd = list(letters+numbers+symbols)
random.shuffle(pwd)
password = "".join(pwd)
print("Here is your password:\t",password)
if len(password)<=6:
    print("Your password is weak")
elif len(password)==7:
    print("Your password stregth is medium")
else:
    print("Your password is strong")
