import regex  # Combiner
from Crypto.Cipher import AES  # AES package from Pycryptodome
from secrets import token_bytes  # Key generator

""""
Dictionaries--
    1. Binary
    2. Morse
    3. Marathi
"""

Binary = {            # Alphabets(Small&Big) = 52 , Numbers = 10, Symbols = 29
   "a": "01100001",
   "b": "01100010",
   "c": "01100011",
   "d": "01100100",
   "e": "01100101",
   "f": "01100110",
   "g": "01100111",
   "h": "01101000",
   "i": "01101001",
   "j": "01101010",
   "k": "01101011",
   "l": "01101100",
   "m": "01101101",
   "n": "01101110",
   "o": "01101111",
   "p": "01110000",
   "q": "01110001",
   "r": "01110010",
   "s": "01110011",
   "t": "01110100",
   "u": "01110101",
   "v": "01110110",
   "w": "01110111",
   "x": "01111000",
   "y": "01111001",
   "z": "01111010",
   "A": "01000001",
   "B": "01000010",
   "C": "01000011",
   "D": "01000100",
   "E": "01000101",
   "F": "01000110",
   "G": "01000111",
   "H": "01001000",
   "I": "01001001",
   "J": "01001010",
   "K": "01001011",
   "L": "01001100",
   "M": "01001101",
   "N": "01001110",
   "O": "01001111",
   "P": "01010000",
   "Q": "01001111",
   "R": "01010010",
   "S": "01010011",
   "T": "01010100",
   "U": "01010101",
   "V": "01010110",
   "W": "01010111",
   "X": "01011000",
   "Y": "01011001",
   "Z": "01011010",
   '/': "01011011",
   '\\': "01011110",
   "'": "01011111",
   "<": "010101",
   " ": "04040",
   ">": "010101",
   # ";":"010101",
   "`": "010101",
   "~": "010101",
   "!": "010101",
   "@": "010101",
   "#": "010101",
   "$": "010101",
   "^": "010101",
   "&": "010101",
   "*": "010101",
   "(": "010101",
   ")": "010101",
   "-": "010101",
   "_": "010101",
   "=": "010101",
   "+": "010101",
   "?": "010101",
   ":": "010101",
   ";": "010101",
   "{": "010101",
   "[": "010101",
   "}": "010101",
   "]": "010101",
   "|": "010101",
   "0": "010101",
   "1": "010101",
   "2": "010101",
   "3": "010101",
   "4": "010101",
   "5": "010101",
   "6": "010101",
   "7": "010101",
   "8": "010101",
   "9": "010101",
}

MORSE = {
    # 'A':'अ',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-'
    }

MARATHI = {
   "a": "के",
   "b": "कू",  # 36, 10  13 49  52
   "c": "कु",
   "d": "की",
   "e": "कि",
   "f": "का",
   "g": "अः",
   "h": "अं",
   "i": "औ",
   "j": "ओ",
   "k": "ऐ",
   "l": "ए",
   "m": "ऊ",
   "n": "उ",
   "o": "ई",
   "p": "इ",
   "q": "आ",
   "r": "अ",
   "s": "ज्ञ",
   "t": "क्ष",
   "u": "ळ",
   "v": "ह",
   "w": "स",
   "x": "श",
   "y": "व",
   "z": "ल",
   "A": "क",
   "B": "ख",
   "C": "ग",
   "D": "घ",
   "E": "च",
   "F": "छ",
   "G": "ज",
   "H": "झ",
   "I": "त्र",
   "J": "ट",
   "K": "ठ",
   "L": "ड",
   "M": "ढ",
   "N": "ण",
   "O": "त",
   "P": "थ",
   "Q": "द",
   "R": "ध",
   "S": "न",
   "T": "प",
   "U": "फ",
   "V": "ब",
   "W": "भ",
   "X": "म",
   "Y": "य",
   "Z": "र",
  # " ":" ",
   # ";":";",
   "`": "`",
   "~": "~",
   "!": "!",
   "@": "@",
   "#": "#",
   "$": "$",
   "%": "%",
   "^": "^",
   "&": "&",
   "*": "*",
   "(": "(",
   ")": ")",
   "-": "-",
   "_": "_",
   "=": "=",
   "+": "+",
   "[": "[",
   "{": "{",
   "]": "]",
   "}": "}",
   "|": "|",
   "\\": "\\",
   ";": ";",
   ":": ":",
   "'": "'",
   ",": ",",
   "<": "<",
   ".": ".",
   ">": ">",
   "/": "/",
   "?": "?",
   "0": "०",
   "1": "१",
   "2": "२",
   "3": "३",
   "4": "४",
   "5": "५",
   "6": "६",
   "7": "७",
   "8": "८",
   "9": "९",

}

# Key generation
key = token_bytes(16)
print("Key-", key)


# AES Encryption
def encrypt_AES(msg):  # Encryption algorithm
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    print(nonce)
    print(tag)
    return nonce, ciphertext, tag


nonce, ciphertext, tag = encrypt_AES(input('Enter a message: '))
print(f'Cipher text: {ciphertext}')

key = str(b'\x8dFj+\x01ul\x7fP9\x87w\xb3H\x7f\xcb')
nonce = str(b'x\x947_\xae\xad\xe3\xf0T\xac\x18\xb3\x08\x9a\xa0\xba')
tag = str(b'\x8fB\xd2\xa3+\x12p\xd5\x8dz!\xa9U\xdb\xd5x')
ciphertext = str(b'\xac\x11;\x0bm')  #HELLO
# encryption_1(key)
# encryption_marathi(key)
# ko=str(कू'\श८कीछओ+\श०१ळए\श७काथ९\श८७स\शकू३झ\श७का\शकुकू')
# message='\श८कीछओ+\श०१ळए\श७काथ९\श८७स\शकू३झ\श७का\शकुकू'



# AES Decryption
def decrypt(message):
    # divide your string into grapheme clusters because it actually contains both letters and nonspacing combining mark
    bring_together_matra = regex.findall(r'\X', message)
    dec = ''
    for letter in bring_together_matra:
        for key, value in MARATHI.items():
             if letter == value:
               dec += key
    print("b'\\"+dec)

#Binary
def Binary_Encrytion(insert_message):
    cipher = ''
    for letter in insert_message:
        if letter != ' ':
             # Looks up the dictionary and adds the
            # correspponding binary code
            # along with a space to separate
            # binary codes for different characters
            cipher+=Binary[letter]+' '
        else:
            cipher += ' '


    print(cipher)    

#Morse
def Morse_Encryption(message):
    message=message.upper()
    cipher = ''
    for letter in message:
        if letter != ' ':
  
            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
    print(cipher)


#Marathi    
def encryption_marathi(insert_message):
    cipher=''
    for letter in insert_message:
       if letter != ' ':
            cipher+=MARATHI[letter]
       else:
              cipher += ' '
    cipher=cipher          
    print(cipher[1:]) 
    
    
def encryption_2(insert_message):
    # string reverse
    rev_string = "".join(reversed(insert_message))
    # swapping of even and odd elements
    b=list(rev_string.split())
    s=len(b)
    if s%2!=0:
        s=s-1
    for i in range(0,s,2):
        b[i],b[i+1]=b[i+1],b[i]
    print("List after swapping :",b)
# re-swapping
    s=len(b)
    if s%2!=0:
        s=s-1
    for i in range(0,s,2):
        b[i+1],b[i]=b[i],b[i+1]
    print("List after swapping :",b)
# list to string
    string=""
    for element in b:
     string+=element+" "




