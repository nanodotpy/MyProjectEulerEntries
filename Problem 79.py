derivatives = [line.rstrip('\n') for line in open('Problem 79.txt')]    

digits = {'7', '2', '6', '0', '9', '3', '8', '1'}  

dico = {'7' : [] , '2' : [] , '3' : [], '1' : [], '6' : [], '0' : [] , '8' : [], '9' : []}

for a in range(len(derivatives)) :  
    for i in digits :                                                    
        if i in derivatives[a] and derivatives[a].index(i) == 1  :
            dico.setdefault("{}".format(i)).append(int(derivatives[a][0]))
        if i in derivatives[a] and derivatives[a].index(i) == 2  :
            dico.setdefault("{}".format(i)).append(int(derivatives[a][0]))
            dico.setdefault("{}".format(i)).append(int(derivatives[a][1]))
        
set7 = {value for value in dico['7']}

set3 = {value for value in dico['3']}  

set2 = {value for value in dico['2']}
                                                                #stupid program
set9 = {value for value in dico['9']}

set8 = {value for value in dico['8']}

set1 = {value for value in dico["1"]}

set6 = {value for value in dico['6']}  

set0 = {value for value in dico['0']}

print(set7)
print(set2)
print(set3)
print(set6)
print(set9)                                     #then used my BRAIN
print(set1)
print(set8)
print(set0)
    