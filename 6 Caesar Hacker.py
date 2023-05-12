print("\n\t\t\tCaesar Cipher Hacker!!!\n")

message = input("Enter the encrypted Caesar cipher message to hack.\n")
print("The decoded for different shifts are given below:\n")
for shift in range(0,27):
    decrypted_message = ""
    for i in message:
        if i.isalpha():
            decrypted_message += chr(ord(i)-shift)
        else:
            decrypted_message += i
        
    print("Key #{}:     {}\n".format(shift,decrypted_message))
    




