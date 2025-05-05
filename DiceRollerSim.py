import random

while True:
    choice = input("Roll dice? (Y/N): ")
    if choice == "N" or choice == "n":
        break
    print(random.randint(1,6))