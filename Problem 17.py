import inflect
import re


p = inflect.engine()

inletters = []

for a in range(1,1001) :
    

    inletters.append(p.number_to_words(a))
    
string = ''.join(inletters)

final = re.sub('[^A-Za-z0-9]+', '', string)


print(len(final))