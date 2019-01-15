for a in range(1000,0,-1):
    for b in range(1000,0,-1):
        if str(a*b) == str(a*b)[::-1]:
            print(a*b)
            break
    else :
        continue
    break
       
#
