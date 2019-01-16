def fibo(a = 1,b = 1) :
    fibo = [a,b]
    while len(str(fibo[-1])) < 1000 :
        fibo.append(fibo[-1]+fibo[-2])
        
    print(len(fibo))
    
if __name__ == "__main__" :
    fibo()