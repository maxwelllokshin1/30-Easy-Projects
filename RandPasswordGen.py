import random
import time
print("Printing random password...")

password = ""

while len(password) != 16:
    password += chr(random.randint(33,126))

print(password)