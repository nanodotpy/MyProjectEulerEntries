def nombre_de_partitions(n, k):
    if n < k:
        return 0                                #Quite slow but works perfectly
    if n == k or k == 1:
        return 1
    if n > k > 1:
        return nombre_de_partitions(n-1, k-1) + nombre_de_partitions(n-k, k) 

total = 0

for k in range(1,100):
    total += nombre_de_partitions(100,k)
    
print(total)