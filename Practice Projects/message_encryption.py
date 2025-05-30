import random 
import string


chars = string.punctuation + string.digits + string.ascii_letters + " "

chars = list(chars)

#key is a shuffled version of chars
key = chars.copy()
random.shuffle(key)


#Encryption process
plaintext = input("Enter the message to encrypt: ")
ciphertext = ""

for letter in plaintext:
    index = chars.index(letter)
    ciphertext += key[index]


print(f"Encrypted Message: {ciphertext}")


# Decryption process
ciphertext = input("Enter the message to decrypt: ")
plaintext = ""

for letter in ciphertext:
    index = key.index(letter)
    plaintext += chars[index]


print(f"Encrypted Message: {ciphertext}")
print(f"Decrypted Message: {plaintext}")