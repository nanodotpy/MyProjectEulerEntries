import time
from collections import Counter
 
time1 = time.time()
 
def main():
    CUBES = [a**3 for a in range(1, 10000)]
    CUBES_DIGITS = [Counter(str(number)) for number in CUBES]
    counter = 0
    for a in CUBES_DIGITS:
        if CUBES_DIGITS.count(a) > 4:
            return CUBES[counter]
        counter += 1
        
if __name__ == '__main__':
    print(main())
    print(time.time() - time1)