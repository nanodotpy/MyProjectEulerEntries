import numpy as np

with open("Problem 81.txt", 'r') as file:
    coefs = file.readlines()

for a in range(len(coefs)):
    coefs[a] = coefs[a].replace("/n", "")
    coefs[a] = coefs[a].split(',')
    for i in range(len(coefs[a])):
        coefs[a][i] = int(coefs[a][i])

matrix = np.array(coefs, dtype = 'int')

infini = sum([matrix.item(n) for n in range(6400)])
        
dico = {(79, 79) : dict()}

sommet0 = (0, 0)

for n in range(6401):
    if n//80 +1 < 80 and n%80 +1 < 80:
        dico[(n//80, n%80)] = {(n//80 + 1, n%80) : matrix[n//80 +1, n%80], (n//80, n%80 +1) : matrix[n//80, n%80 +1]}
    elif n//80 == 79 and not n%80 == 79:
        dico[(n//80, n%80)] = {(n//80, n%80 +1) : matrix[n//80, n%80 +1]}
    elif n%80 == 79 and not n//80 == 79:
        dico[(n//80, n%80)] = {(n//80 +1, n%80) : matrix[n//80 +1, n%80]}
                
# ---------------------------------------------------------
        
s_connu = {sommet0 : [0, [sommet0]]}

s_inconnu = {k :[infini, ''] for k in dico if k != sommet0}

for suivant in dico[sommet0]:
    s_inconnu[suivant] = [dico[sommet0][suivant], sommet0]
    
# --------------------------------------------------------

while s_inconnu and any(s_inconnu[k][0] < infini for k in s_inconnu):
    u = min(s_inconnu, key = s_inconnu.get)
    longueur_u, precedent_u = s_inconnu[u]
    
    for v in dico[u]:
        if v in s_inconnu:
            d = longueur_u + dico[u][v]
            if d < s_inconnu[v][0]:
                s_inconnu[v] = [d, u]
    s_connu[u] = [longueur_u, s_connu[precedent_u][1] + [u]]
    del s_inconnu[u]
    
total = 0

for i in s_connu[(79,79)][1]:           
    total += matrix[i[0], i[1]]
    
print(total) 
    
