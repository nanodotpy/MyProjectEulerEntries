triangle = [line.rstrip('\n') for line in open('Problem 67.txt')]

def string_split(string) :
    return [int(string[i:i+2]) for i in range(0, len(string), 2 )]


triangle = [element.replace(" ", "") for element in triangle]


triangle =  [string_split(element) for element in triangle]

a = 0
        
for i in range(len(triangle)-1,0,-1) :                                  #My solution for problem 18 was actually BAD
    for e in range(0,len(triangle[i])-1) :
        maximum = max(triangle[i][e],triangle[i][e+1])
        triangle[i-1][e] += maximum
    
print(triangle[0])