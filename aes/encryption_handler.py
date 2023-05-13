from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

data = b'This is a secret string'

key = get_random_bytes(48)
cipher = AES.new(key, AES.MODE_SIV)
ciph_object = cipher.encrypt_and_digest(data)
ciph_text = ciph_object[0]

ciph_str = str(ciph_object[0])
print(ciph_str)

ciph_bytes = eval(ciph_str)
print(ciph_bytes)

print(ciph_bytes == ciph_text)
print("{}".format(ciph_text))
# ciph_dict = {
#     'ciphertext' : ciph_object[0],
#     'tag' : "{}".format(ciph_object[1])
# }
# print(type(ciph_dict['tag']))
# print(type(ciph_dict['ciphertext']))

# print(ciph_dict['ciphertext'].decode('utf-8'))


# # print("Ciphertext : {} \nTag : {}".format(ciphertext,tag))

# cipher = AES.new(key, AES.MODE_SIV)
# ciphertext = ciph_dict['ciphertext'].encode('utf-8')
# tag = ciph_dict['tag'].encode('utf-8')
# data = cipher.decrypt_and_verify(ciphertext, tag)
# print("Decrypted data : {}".format(data))