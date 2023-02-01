alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text,shift):
  ciphar_text=""
  for i in text:
    indexNo=alphabet.index(i)
    letter=alphabet[indexNo+shift]
    ciphar_text+=letter
    
    
  print(f"The encoded text is {ciphar_text}")        
 
   
def decrypt(text,shift):
  plain_text=""
  for i in text:
    IndexNo=alphabet.index(i)
    letter=alphabet[IndexNo-shift]
    plain_text+=letter
  print(f"The decoded text is {plain_text}")    

if direction=="encode":
  encrypt(text,shift)
elif direction=="decode":
  decrypt(text,shift)
else :
  print("Type 'encode' to encrypt, type 'decode' to decrypt:\n")