alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(direction,text,shift):
  ciphar_text=""
  if(direction=="decode"):
      shift*=-1 
  for i in text:
    indexNo=alphabet.index(i)
    letter=alphabet[indexNo+shift]
    ciphar_text+=letter
    
  print(f"The {direction} text is {ciphar_text}")        

caesar(direction,text,shift) 