def encrypt(text,shift): 
    result = "" 
    for i in range(len(text)): 
        char = text[i] 
        if (char.isupper()): 
            result += chr((ord(char) + shift - 65) % 26 + 65) 
        else: 
            result += chr((ord(char) + shift - 97) % 26 + 97) 
    return result 

crypted = encrypt("This is plain text", 4)
print(crypted)