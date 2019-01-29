import string
from itertools import product
import collections

file = open("Problem 59.txt")
text = str(file.read())
numbers = text.split(',')
numbers = [int(number) for number in numbers]

chars = ""

for number in numbers :
    chars = chars + chr(number)
    
characters = list(string.ascii_lowercase)

keys = list(product(characters,repeat = 3))

keys = [('').join(element) for element in keys]

def decryption(listofascii,stringkey) :
    result = ""
    
    for i in range(len(listofascii)) :
        result += chr(listofascii[i] ^ ord(stringkey[i%3]))
        
    return result
"""   
for key in keys :
    c = collections.Counter(decryption(numbers[:100],key))
    if c[' '] > 10 :                                                                    # Found the key using this 
        print("{} : {}".format(key,decryption(numbers[:100],key)))                      

""" 

key = "god"

decoded = decryption(numbers,key)

asciisum = 0

for char in decoded :
    asciisum += ord(char)
    
print(asciisum)
