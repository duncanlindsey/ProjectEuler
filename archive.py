def isPrime(n):
    i = 2
    while i < (n/i):
        if n % i == 0:
            return False
        i += 1
    return True

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