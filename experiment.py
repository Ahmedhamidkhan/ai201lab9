def encrypt(message, key):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: 
            letter_index = (alpha.find(letter) + key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result

def decrypt(message, key):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for letter in message:
        if letter in alpha: 
            letter_index = (alpha.find(letter) - key) % len(alpha)

            result = result + alpha[letter_index]
        else:
            result = result + letter

    return result


message = "DEFENDTHEFORT"
key = 7
encr=encrypt(message, key)
decr=decrypt(encr, key)
print (f"Plain Text : {message}")
print (f"Shift pattern :  {key}")
print (f"Cipher encrypt: {encr}")
print (f"Cipher decrypt: {decr}")