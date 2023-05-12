print("\n\n\n \t Welcome to Treasure Island!\n\n")
print("\n\tYour mission is to find the treasure.\n")

print("Left or right?")
ans = input("Type Right/left:\t").lower()


if ans =="left":
    print("Nice ,you made it to the next level!\n\n")
    print("Your map shows that you need to get to Treasure Island, you can wait to board a ship or swim accross the sea, pick one.")
    ans = input("Type Swim/Wait:\t").lower()

    if ans =="wait":
        print("Nice, you made it to the next level, you're pretty good at this!")
        print("Now that you've made it to Treasure Island, you can dig or search the cave.")
        ans = input("Type Dig/Cave:\t").lower()

        if ans =="dig":
            print("You've found the treasure\n\n\t\tYou win!")
        
        else:
            print("You are eaten by a shark.\n\n\t You Lost!!!")

    else:
        print("You are eaten by a bear.\n\n\t You Lost!!!")


else:
    print("Sonic the Hedgehog got first to the island.\n\n\t\tYou Lost!!!")

