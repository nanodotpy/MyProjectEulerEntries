def char_position(letter):
    return ord(letter) - 96


triangles = [(n*(n+1))//2 for n in range(100000)]

def triangle_word(word) :
    word = (word.lower())
    score = 0
    for letter in word :
        score += char_position(letter)
    if score in triangles :
        return True
    else :
        return False
    
amount = 0 

file = open("Problem 42.txt","r")

names = file.read()

names = names.replace(',',' ')

names = names.replace('"','')

namelist = list(names.split(' '))

for word in namelist :
    if triangle_word(word) :
        amount += 1
        
print(amount)