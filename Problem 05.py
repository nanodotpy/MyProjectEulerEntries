def j20(a) :
    for b in range(2,21):
        if a % b == 0 and b == 20 :
            return True
        elif a % b != 0 :
            return False
        
        
        
z = 2520        
        
while not j20(z) :
    z += 20

else : print(z)
    
        

            
