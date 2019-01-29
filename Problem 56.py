def digital_sum(number) :
    number = int(number)
    number = str(number)
    listnumber = list(number)
    listnumber = [int(element) for element in listnumber]
    return sum(listnumber)

somme = []


for a in range(1,100) :
    for b in range(0,100) :
        somme.append(digital_sum(a**b))
        
print(max(somme))
        
        