def squares(number) :
    return sum(int(a)**2 for a in str(number))

def is_unhappy(number) :
    while True :
        number = squares(number)
        if number == 4 :
            return True
        if number == 1 :
            return False
        
lowhappy = []

for a in range(1,568) :
    if not is_unhappy(a) :
        lowhappy.append(a)
        
total = 0    
        
for e in range(1,10000000) :
    if squares(e) not in lowhappy :
        total += 1
        
print(total)
        
        