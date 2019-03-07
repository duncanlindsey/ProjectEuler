'''
================================
Problem 3 - Largest Prime Factor
================================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

test = 600851475143

def primeFactors(n):
    primes = []
    i = 2
    while i <= n:
        if n % i == 0:
            primes.append(i)
            n = n/i
        else:
            i += 1
    return primes

print (primeFactors(test)[-1])

