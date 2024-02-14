import string
import random

letters = string.ascii_letters
digit = string.digits
symbol = string.punctuation

print("-"*100)
length = int(input("Enter the length of Password : "))
difficulty = int(
    input("Select password difficulty : \n 1) Low \n 2) Medium \n 3) Difficult  \n\n Select (1/2/3) : "))

if difficulty == 1:
    characters = letters
elif difficulty == 2:
    characters = letters + digit
elif difficulty == 3:
    characters = letters + digit + symbol
else:
    characters = letters + digit
    print("Wromg selection, Default selected Medium.")


password = "".join(random.choices(characters,k= length))
print("-"*100)
print("Password : "+password)
print("-"*100)