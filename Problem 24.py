import itertools
  
permus = list(itertools.permutations(str(1234567890)))

permus = [int(''.join(value)) for value in permus]

permus.sort()

print(permus[999999])
