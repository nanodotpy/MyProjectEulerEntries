def char_position(letter):
    return ord(letter) - 96

def score(name) : 
    
    listofletters = [letter for letter in name]
    score = [char_position(letter) for letter in listofletters]
    
    return sum(score)
    
file = open("Problem 22.txt", 'r')

names = file.read()

names = names.replace(',',' ')

names = names.replace('"','')

namelist = list(names.split(' '))

namelist = sorted(namelist)

scorecounter = 0

for name in namelist : 
    scorecounter += (score(str(name).lower())*(namelist.index(name)+1))
    
    
print(scorecounter)
    




