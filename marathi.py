import regex                               #Combiner
from Crypto.Cipher import AES
from secrets import token_bytes

MARATHI= {
   "a":"के",
   "b":"कू", ##36, 10  13 49  52
   "c":"कु",
   "d":"की",
   "e":"कि",
   "f":"का",
   "g":"अः",
   "h":"अं",
   "i":"औ",
   "j":"ओ",
   "k":"ऐ",
   "l":"ए",
   "m":"ऊ",
   "n":"उ",
   "o":"ई",
   "p":"इ",
   "q":"आ",
   "r":"अ",
   "s":"ज्ञ",
   "t":"क्ष",
   "u":"ळ",
   "v":"ह",
   "w":"स",
   "x":"श",
   "y":"व",
   "z":"ल",
   "A":"क",
   "B":"ख",
   "C":"ग",
   "D":"घ",
   "E":"च",
   "F":"छ",
   "G":"ज",
   "H":"झ",
   "I":"त्र",
   "J":"ट",
   "K":"ठ",
   "L":"ड",
   "M":"ढ",
   "N":"ण",
   "O":"त",
   "P":"थ",
   "Q":"द",
   "R":"ध",
   "S":"न",
   "T":"प",
   "U":"फ",
   "V":"ब",
   "W":"भ",
   "X":"म",
   "Y":"य",
   "Z":"र",
  # " ":" ",
   ";":";",
   "`":"`",
   "~":"~",
   "!":"!",
   "@":"@",
   "#":"#",
   "$":"$",
   "%":"%",
   "^":"^",
   "&":"&",
   "*":"*",
   "(":"(",
   ")":")",
   "-":"-",
   "_":"_",
   "=":"=",
   "+":"+",
   "[":"[",
   #"{":"{",  
   "]":"]",
   #"}":"}",
   "|":"|",
   "\\":"\\" ,
   #";":";",
   ":":":",       
   "'":"'",
   ",":",",
   "<":"<",
   ".":".",
   ">":">",
   "/":"/",
   "?":"?", 
   "0":"०",
   "1":"१",
   "2":"२",
   "3":"३",
   "4":"४",
   "5":"५",
   "6":"६",
   "7":"७",
   "8":"८",
   "9":"९",

   
}

def encryption_marathi(insert_message):
    cipher=''
    for letter in insert_message:
       if letter != ' ':
            cipher+=MARATHI[letter]
       else:
              cipher += ' '
      #cipher=cipher[4:]         
    return "Marathi-encrypt" + "'" + cipher[4:]         # Warning to remove - R prefix ,required


msg=str(b'\x8dFj+\x01ul\x7fP9\x87w\xb3H\x7f\xcb')
encryption_marathi(msg)




def decrypt(message):
    bring_together_matra=regex.findall(r'\X',message)     #divide your string into grapheme clusters because it actually contains both letters and nonspacing combining mark
    dec=''
    for letter in bring_together_matra:  
        for key, value in MARATHI.items():
             if letter == value:
               dec+=key
    print("Marathi-Decrypt-" + "b'\\" +dec)           

#kdl='श८कीछओ+\श०१ळए\श७काथ९\श८७स\शकू३झ\श७का\शकुकू' # Warning to remove - R prefix ,required
#decrypt(kdl)













