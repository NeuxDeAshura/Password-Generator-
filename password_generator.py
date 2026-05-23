import random
import string

while True:
    length = int(input("Enter the length of your password(1-16):"))

    if 1 <= length <= 16:
        break
    else:
        print("Invalid input, please enter a number between 1-16.")

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

    print("Generated Password:", password)

print("- - - E X I T I N G  A P P L I C A T I O N - - -")
exit()
