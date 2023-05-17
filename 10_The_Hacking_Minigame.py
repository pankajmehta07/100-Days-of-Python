import random
import string

data = ['RESOLVE','CHICKEN','DESPITE','ADDRESS','DISPLAY','REFUGEE','PENALTY','STUDENT','IMPROVE','IMPRESS','DRAWING','GRANTED','HACKING','PROGRAM','PROJECT','AIRLINE','AIRPLAN','ANOTHER','ARRANGE','ARTICLE','SKILLED','THOUGHT','WILLING','VARIOUS','VEHICLE','UNIFORM','TEACHER','RELEASE','RECOVER','TENSION','PASSIVE','ORGANIC','INTENSE','CURRENT','MANAGER','FOUNDER','IMAGINE','JUSTICE','JUSTIFY','INCLUDE','HISTORY','CRICIAL']



print("\n\n\t\tHacking MInigame.\n")
print("Find the password in the computer's memory: ")
secret = random.choice(data)
data.remove(secret)
secret_number = random.randint(0,9)
for i in range(12):
    
    symbol = ""
    for i in range(7):
        symbol += random.choice(string.punctuation)
    hexa = str(hex(id(data)))[:6]
    if i == secret_number:
        word = secret
    else:
        word = random.choice(data)
        data.remove(word)
    num = random.randint(1,5)
    print(hexa+symbol[:num]+word+symbol[num:],end="\t\t")

for i in range(10):
    guess = input(f"\n\nEnter password ({10-i} tries remaining):\t").upper()
    
    if guess==secret:
        print("\n\tACCESS GRANTED\n")
        won = True
        break
    else:
        guess = guess[:7]
        won = False
        count = 0
        for letter in guess:
            if letter in secret:
                count +=1
    print(f"Access Denied ({count}/7 correct)")
if won == False:
    print("\n\tCOMPUTER LOCKED. Too many attempts")