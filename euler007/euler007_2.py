#!/bin/python3
import time
from math import sqrt

count = 0

def get_prime(primes, N):
    global count
    if N < len(primes):
        return primes[N-1]
    candidate = primes[-1]
    while len(primes) != N:
        candidate += 2
        count += 1
        if count == 5:
            count = 0
            candidate += 2
        s = int(sqrt(candidate))
        #print("candidate = %d, primes = %s" % (candidate, primes))
        for p in primes[1:]:
            if p > s:
                primes.append(candidate)
                break
            if (candidate % p) == 0:
                break
    return primes[-1]

start = time.time()
primes = [2, 3, 5]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(get_prime(primes, n))
assert(get_prime(primes, 168) == 997)
assert(get_prime(primes, 10000) == 104729)
print("Computation time: %f seconds" % (time.time() - start))
#print(primes)
