import numpy as np

def encrypt(message):
    # Using the equation C = KP mod26
    # Replace spaces with nothing
    message = message.replace(" ", "")
    # Ask for keyword and get encryption matrix
    K = make_key()
    # Append zero if the messsage isn't divisble by 2
    length_check = len(message) % 2 == 0
    if not length_check:
        message += "0"
    # Populate message matrix
    P = create_matrix_of_integers_from_string(message)
    message_length = int(len(message) / 2)
    # Calculate P * Key
    encrypted_msg = ""
    for i in range(message_length):
        # Dot product
        row_0 = P[0][i] * K[0][0] + P[1][i] * K[0][1]
        # Modulate and add 65 to get back to the A-Z range in ascii
        integer = int(row_0 % 26 + 65)
        # Change back to chr type and add to text
        encrypted_msg += chr(integer)
        # Repeat for the second column
        row_1 = P[0][i] * K[1][0] + P[1][i] * K[1][1]
        integer = int(row_1 % 26 + 65)
        encrypted_msg += chr(integer)
    return encrypted_msg

def decrypt(encrypted_msg):
    # Using the equation P = K(inverse)C mod26
    K = make_key()
    # Inverse matrix
    determinant = K[0][0] * K[1][1] - K[0][1] * K[1][0]
    determinant = determinant % 26
    multiplicative_inverse = find_multiplicative_inverse(determinant)
    K_inverse = K
    # Finding adjoint
    K_inverse[0][0], K_inverse[1][1] = K_inverse[1, 1], K_inverse[0, 0]
    K[0][1] *= -1
    K[1][0] *= -1
    
    for row in range(2):
        for column in range(2):
            K_inverse[row][column] *= multiplicative_inverse
            K_inverse[row][column] = K_inverse[row][column] % 26

    P = create_matrix_of_integers_from_string(encrypted_msg)
    msg_len = int(len(encrypted_msg) / 2)
    decrypted_msg = ""
    for i in range(msg_len):
        # Dot product
        column_0 = P[0][i] * K_inverse[0][0] + P[1][i] * K_inverse[0][1]
        # Modulate and add 65 to get back to the A-Z range in ascii
        integer = int(column_0 % 26 + 65)
        # Change back to chr type and add to text
        decrypted_msg += chr(integer)
        # Repeat for the second column
        column_1 = P[0][i] * K_inverse[1][0] + P[1][i] * K_inverse[1][1]
        integer = int(column_1 % 26 + 65)
        decrypted_msg += chr(integer)
    if decrypted_msg[-1] == "0":
        decrypted_msg = decrypted_msg[:-1]
    return decrypted_msg

def find_multiplicative_inverse(determinant):
    multiplicative_inverse = -1
    for i in range(26):
        inverse = determinant * i
        if inverse % 26 == 1:
            multiplicative_inverse = i
            break
    return multiplicative_inverse


def make_key():
     # Function to confirm cipher determinant is relatively prime to 26 and only alphabets are given
    determinant = 0
    K = None
    while True:
        cipher = input("Input 4 letter cipher: ")
        K = create_matrix_of_integers_from_string(cipher)
        determinant = K[0][0] * K[1][1] - K[0][1] * K[1][0]
        determinant = determinant % 26
        inverse_element = find_multiplicative_inverse(determinant)
        if inverse_element == -1:
            print("Determinant is not relatively prime to 26, uninvertible key")
        elif np.amax(K) > 26 and np.amin(K) < 0:
            print("Only a-z characters are accepted")
            print(np.amax(K), np.amin(K))
        else:
            break
    return K

def create_matrix_of_integers_from_string(string):
    # Map string to a list of integers a/A <-> 0, b/B <-> 1 ... z/Z <-> 25
    integers = [chr_to_int(c) for c in string]
    length = len(integers)
    M = np.zeros((2, int(length / 2)), dtype=np.int32)
    iterator = 0
    for column in range(int(length / 2)):
        for row in range(2):
            M[row][column] = integers[iterator]
            iterator += 1
    return M

def chr_to_int(char):
    # Converting char and getting in range of 0-25
    char = char.upper()
    integer = ord(char) - 65
    return integer

if __name__ == "__main__":
    option = int(input("Select \n 1.Encryption \n 2.Decryption \n"))
    if(option==1):
        msg = input("Message: ")
        encrypted_msg = encrypt(msg)
        print(encrypted_msg)
    elif(option==2):
        cipherText = input("Cipher Text: ")
        decrypted_msg = decrypt(cipherText)
        print(decrypted_msg)