from Crypto.Cipher import AES
from secrets import token_bytes

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False


#input given was --HELLO
#variables that were generated are below
#when generated values are provided to the decrypt function ,it shows fales how do i fix it,so when i give the values i get text HELLO back again

key= b'\x8dFj+\x01ul\x7fP9\x87w\xb3H\x7f\xcb'
nonce= b'x\x947_\xae\xad\xe3\xf0T\xac\x18\xb3\x08\x9a\xa0\xba' # CO-ordinates of Matrix
tag= b'\x8fB\xd2\xa3+\x12p\xd5\x8dz!\xa9U\xdb\xd5x'            # --^--
ciphertext=b'\xac\x11;\x0bm' # HELLO


plaintext = decrypt(nonce, ciphertext, tag)

print(f'Cipher text: {ciphertext}')
if not plaintext:
    print('Message is corrupted')       #if anything else gets added up in the process
else:
    print(f'Plain text: {plaintext}')