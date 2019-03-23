from collections import Counter
from math import sqrt

str_numbers = [str(a) for a in range(10)]

def carrés(a, b):
    for i in range(int(sqrt(a)), int(sqrt(b))+2):
        carré = i**2
        if a < carré < b:
            yield carré


with open("problem 98.txt") as words:
    words = words.read()
    
words = words.split('","')

counters = {a: Counter(a) for a in words}

anagrams = []

for a, x in counters.items():
    if (list(counters.values())).count(x) > 1:
        anagrams += [a]
                
for a in anagrams:
    for b in anagrams:
        if a == b[::-1]:
            anagrams.remove(a)
            anagrams.remove(b)
            
anagrams = [(a,b) for a in anagrams for b in anagrams if Counter(a) == Counter(b) and a != b]
            
lens = {word: len(word) for word in anagrams}

longest = []

for word, length in lens.items():
    if length == max(lens.values()):
        longest += [word]

def starf(word1, word2):
    counter1, counter2 = Counter(word1), Counter(word2)
    assert counter1 == counter2
    len1 = len(counter1)
    vals = list(counter1.values())
    squares = list(carrés(10**(len1-1), 10**(len1)))
    counts = {a: Counter(str(a)) for a in squares}
    final_squares = []
    for i, j in counts.items():
        if list(counter1.values()) == list(j.values()):
            final_squares += [i]
    pairs = [(a,b) for a in final_squares for b in final_squares if Counter(str(a)) == Counter(str(b))]
    result = []
    for pair in pairs:
        replacements1 = {a : b for a, b in zip(word1, str(pair[0]))}
        replacements2 = {a : b for a, b in zip(word2, str(pair[1]))}
        if replacements1 == replacements2:
            result += [pair]
    return result
            

for i, j in anagrams:
    print(starf(i, j))
    
# max : 18769 et mercé la zone
    

        

            
    