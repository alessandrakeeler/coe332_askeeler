

def primes():
    for i in range(3, 101):
        for j in range(2, int(i/2) + 1 ):
            if i%j == 0:
                break
         
        else:
            print(str(i) + " is prime")
            
primes()