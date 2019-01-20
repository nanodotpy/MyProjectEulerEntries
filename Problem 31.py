one = 1
two = 2
five = 5
ten = 10
twt = 20
fft = 50
oneh = 100
twoh = 200


ways  = 1


for b in range(0,3) :
    for c in range(0,5) :
        for d in range(0,11) :
            for e in range(0,21) :
                for f in range(0,41) :
                    for g in range(0,101) :
                        for h in range(0,201) :
                            if b*oneh + c*fft + d*twt + e*ten + five*f + two*g + h*one == 200 :
                                ways += 1
    
print(ways)
    
#Works but very BAD