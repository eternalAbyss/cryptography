def encrypt(text, shift):
    result = ""
    textl = []
    textl = [ each + 4 for each in text ]
    print(textl)
    print(shift)

encrypt("this is the first text", 4)