from Crypto.Cipher import AES
from secrets import token_bytes

key = token_bytes(16)           #14 round  = 256 bits random key
#print("Key-",key)


def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)        #Matrix 4x4
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii')) #Converted to ascii code A=10 / binary 1010
    return nonce, ciphertext, tag



nonce, ciphertext, tag = encrypt(input('Enter a message: '))
print("Key-",key)
print(f'Cipher text: {ciphertext}')
print(f'Nonce: {nonce}')
print(f'Tag: {tag}')


