import os
import string

with open('alphabet.txt', 'w') as af:
    af.write(string.ascii_lowercase)

print('Alphabet file is created')