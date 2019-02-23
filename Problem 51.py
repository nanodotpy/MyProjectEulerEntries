from itertools import permutations

permus = list(permutations(range(9),5))

permus = [int(''.join(str(x) for x in y)) for y in permus]

print(permus)