from itertools import count

"""
nobody in the entire universe except me can understand what I did there
thanks god i wont read this script again

it is actually kind of efficient
"""

def triangle(n):
    return int(n*(n+1)/2)

def square(n):
    return int(n**2)

def pentagone(n):
    return int(n*(3*n-1)/2)

def hexagone(n):
    return int(n*(2*n-1))

def heptagone(n):
    return int(n*(5*n-3)/2)

def octogone(n):
    return int(n*(3*n-2))

def are_cyclic(a, b):
    if str(a)[:-3:-1] == str(b)[:2]:
        return (str(a)[:2], str(b)[-2:])
    elif str(b)[:-3:-1] == str(a)[:2]:
        return (str(b)[:2], str(a)[-2:])
    
def minus_key(dictionary, key):
    shallow_copy = dict(dictionary)
    del shallow_copy[key]
    return shallow_copy

def get_name_of_fonction(fonc):
    fonc = fonc.split()
    return fonc[1]

polygonals = [triangle, square, pentagone, hexagone, heptagone, octogone]

poly_strings = {x.__name__ for x in polygonals}

numbers_4_digits = {}

for func in polygonals:
    
    numbers_4_digits[f"{func}"] = []

    for n in count():
        if func(n) > 9999:
            break
        if func(n) > 1000:
            numbers_4_digits[f"{func}"].append(func(n))

dico = {(key.__name__, value.__name__) : [] for key in polygonals for value in polygonals if key != value}

for func in polygonals:
    temp = minus_key(numbers_4_digits, f"{func}")
    for j in numbers_4_digits[f'{func}']:
        for k in temp.keys():            
            for a in temp[k]:
                if str(j)[2:] == str(a)[:2]:
                    dico[(func.__name__, get_name_of_fonction(k))].append((j, a))
                    
liste_de_ses_morts = []
                    
for k in dico.keys():
    temporary = list(dico)
    for i in list(dico):
        if i[0] == k[0] or k[1] == i[1] or k[0] == i[1] or k[1] == i[0]:
            temporary.remove(i)
    for e in dico[k]:
        for merde in temporary:
            for putain in dico[merde]:
                if str(e[1])[-2:] == str(putain[0])[:2]:
                    classes = set(k + merde)
                    reste = tuple(poly_strings - classes)
                    # print(e, putain, reste)
                    for z in dico[(reste[0], reste[1])]:
                        if str(z[0])[:2] == str(putain[1])[2:]:
                            liste_de_ses_morts.append([e[0], e[1], putain[0], putain[1], z[0], z[1]])
                    for z in dico[(reste[1], reste[0])]:
                        if str(z[0])[:2] == str(putain[1])[2:]:
                            liste_de_ses_morts.append([e[0], e[1], putain[0], putain[1], z[0], z[1]])
                                      
for i in liste_de_ses_morts:
    if str(i[5])[2:] == str(i[0])[:2]:
        print(i)
        print(sum(i))
                    