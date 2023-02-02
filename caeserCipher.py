alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']






def caesar(direction,text,shift):
  ciphar_text=""
  if(direction=="decode"):
      shift*=-1 
  for i in text:
    indexNo=alphabet.index(i)
    letter=alphabet[indexNo+shift]
    ciphar_text+=letter
    
  print(f"The {direction} text is {ciphar_text} \n\n")        

import art

print(art.logo);

val=True;
while val:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if(shift>26):
    shift=shift%26
  
  caesar(direction,text,shift) 
  condition =input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
  if(condition !="yes"):
    val=False;
    print("GOOD BYE")
  else:
    print("=============================================================\n\n")