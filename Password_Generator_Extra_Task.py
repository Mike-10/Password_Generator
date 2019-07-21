"""
Extra:

Ask the user how strong they want their password to be.
For weak passwords, pick a word or two from a list.
"""
import random
import time
import string
from random import shuffle

password_strength = {"Strong" : 1, "Weak" : 2}
print(password_strength)
strength = input("How strong do you want your password to be? ")

if strength == "1":
    particle_integer = str(random.randint(0,9))
    particle_upper_letters = random.choice(string.ascii_uppercase)
    particle_lower_letters = random.choice(string.ascii_lowercase)
    particle_punctuation = str(random.choice(string.punctuation))
    length = random.randint(8,12)
    base = [particle_integer,particle_upper_letters,particle_lower_letters,particle_punctuation]

    while length != 0:
        particle_integer = str(random.randint(0,9))
        particle_upper_letters = random.choice(string.ascii_uppercase)
        particle_lower_letters = random.choice(string.ascii_lowercase)
        particle_punctuation = str(random.choice(string.punctuation))
        choices = [particle_integer,particle_upper_letters,particle_lower_letters,particle_punctuation]
        base.append(random.choice(choices))
        length -=1

    shuffle(base)
    password = "".join(base)
    print(password)


elif strength == "2":
    length2 = random.randint(1,4)

    weak_passwords = ["darktown","hilliard","polocyte","carracci","crankier","jungfrau","anoxemia","arillode","roseburg","inchmeal"]
    word_password = random.choice(weak_passwords)

    base2 = []
    base2.append(word_password)

    while length2 != 0:
        particle_integer = random.randint(0,9)
        particle_punctuation = random.choice(string.punctuation)
        choices = [particle_integer,particle_punctuation]
        base2.append(str(random.choice(choices)))
        length2 -=1

    password2 = "".join(base2)
    print("\nYour new password is",password2)
