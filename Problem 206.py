for x in range(int(1.41*10**9),int(1.01*10**9),-10) :
    square = x**2
    if str(square)[2] == '2' and str(square)[4] == '3' and str(square)[6] == '4' and str(square)[8] == '5' and str(square)[10] == '6' and str(square)[12] == '7' and str(square)[14] == '8' and str(square)[16] == '9' and str(square)[18] == '0' :
        print(x,square)
        break
        
        #Absolutely stupid program but works in 3 seconds sooo...
    
        