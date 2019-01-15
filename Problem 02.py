fibo = [1,2]
while fibo[len(fibo)-1] < 4000000 :
    
    fibo.append(fibo[len(fibo)-1]+fibo[len(fibo)-2])


a = 0

for i in range(len(fibo)):
    if fibo[i] % 2 == 0:
        a += fibo[i]
        
print(a)
