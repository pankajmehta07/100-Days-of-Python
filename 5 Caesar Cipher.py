run = True
while run:
    encode_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\t")

    message = input("Type your message:\t").lower()
    shift = int(input("Type the shift number:\t"))

    if encode_decode=="encode":
        encrypted_message = ""
        for i in message:
            if i.isalpha():
                encrypted_message += chr(ord(i)+shift)
            else:
                encrypted_message += i
        print("Here's the encoded result: {}".format(encrypted_message))
    else:
        decrypted_message = ""
        for i in message:
            if i.isalpha():
                decrypted_message += chr(ord(i)-shift)
            else:
                decrypted_message += i
            
        print("Here's the decoded result: {}".format(decrypted_message))
    print("Do you want to run this program again?")
    again = input("Type 'yes' or 'no':\t").lower()

    if again =="no":
        run = False
        print("Goodbye")


