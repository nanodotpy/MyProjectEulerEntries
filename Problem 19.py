import datetime

counter = 0 

for a in range(1901,2001):
    for e in range(1,13) :
        datetime.datetime(a, e, 1)
    
        if datetime.datetime(a,e,1).weekday() == 6 :
            counter += 1
    
print(counter)

