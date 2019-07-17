"""
Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.
"""

import random
import time
import string

start_time = time.time()
length = random.randint(8,12)
base = []

while length != 0:
    particle_integer = random.randint(0,9)
    particle_upper_letters = random.choice(string.ascii_uppercase)
    particle_lower_letters = random.choice(string.ascii_lowercase)
    particle_punctuation = random.choice(string.punctuation)
    choices = [particle_integer,particle_upper_letters,particle_lower_letters,particle_punctuation]
    base.append(str(random.choice(choices)))
    length -=1

password = "".join(base)
print(password)

print("--- %s seconds ---" % (time.time() - start_time))

"""
Extra:

Ask the user how strong they want their password to be.
For weak passwords, pick a word or two from a list.
"""


print ("\nEXTRA TASK\n")

password_strength = {"Strong" : 1, "Weak" : 2}
print(password_strength)
strength = input("How strong do you want your password to be? ")

if strength == "1":
    length = random.randint(8,12)
    base = []

    while length != 0:
        particle_integer = random.randint(0,9)
        particle_upper_letters = random.choice(string.ascii_uppercase)
        particle_lower_letters = random.choice(string.ascii_lowercase)
        particle_punctuation = random.choice(string.punctuation)
        choices = [particle_integer,particle_upper_letters,particle_lower_letters,particle_punctuation]
        base.append(str(random.choice(choices)))
        length -=1

    password = "".join(base)
    print("\nYour new password is",password)
elif strength == "2":
    length2 = random.randint(1,4)

    weak_passwords = ["darktown","hilliard","polocyte","carracci","crankier","jungfrau","anoxemia","arillode","roseburg","inchmeal"]

    print(weak_passwords)
    word = input("Enter a word, use both upper and lower case.\nPlease see suggestions from the list: ")

    base2 = []
    base2.append(word)

    while length2 != 0:
        particle_integer = random.randint(0,9)
        particle_punctuation = random.choice(string.punctuation)
        choices = [particle_integer,particle_punctuation]
        base2.append(str(random.choice(choices)))
        length2 -=1

    password2 = "".join(base2)
    print("\nYour new password is",password2)
