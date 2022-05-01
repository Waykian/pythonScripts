import time

def primeList(limit: int):  #returns a list of primes from 2 to limit
    primes = []
    if (limit < 2):
        return []
    i = 2
    while (i < limit):
        check = True
        for j in primes:
            if (i % j == 0):
                check = False
        if(check):
            primes.append(i)
        i += 1
    return primes

ins = input("Insert a number and I will show you all the primes before it: ")
start = time.time()
print(primeList(int(ins)))
print(f"Time: {time.time() - start}")
    