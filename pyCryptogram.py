def crypt():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    values = keys[-1] + keys[0:-1]

    encryptDict = dict(zip(keys, values))
    decryptDict = dict(zip(values, keys))

    message = input("Enter your message")
    mode = input("Mode: Press <E> for encrypting and <D> for decrypting")

    if mode.upper() == 'E':
        newMessage = ''.join([encryptDict[letter]
                                for letter in message.lower()])
    elif mode.upper() == 'D':
        newMessage = ''.join([decryptDict[letter]
                                for letter in message.lower()])
    else:
        print("Invalid choice")

    return newMessage

print(crypt())

terminate = input("Press any key to exit")
