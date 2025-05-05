import random

place = input("Enter place: ")
person = input("Enter person: ")
object = input("Enter object: ")

stories = (
    f"To get to the {place}, {person} had to jump over obsticles holding nothing but an {object}",
    f"When I found out who {person} was, my {place} changed, leaving me to take care of this {object}",
    f"Some would say {person} plays too many games, not touching enough {object} and staying in the {place} instead"
)

print(stories[random.randint(0, len(stories)-1)])