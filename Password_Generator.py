"""
Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.
"""

import random
import time
import string
from random import shuffle

start_time = time.time()
length = random.randint(8,12)

particle_integer = str(random.randint(0,9))
particle_upper_letters = random.choice(string.ascii_uppercase)
particle_lower_letters = random.choice(string.ascii_lowercase)
particle_punctuation = str(random.choice(string.punctuation))

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

print("--- %s seconds ---" % (time.time() - start_time))
