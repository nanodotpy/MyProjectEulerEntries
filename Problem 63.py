from math import ceil
n = 1
result = 0
limit = 0


while limit < 10:
    limit = int(ceil(10**((n-1)/n)))                    #Needed help  
    result += 10 - limit
    
    n += 1
    
print(result)