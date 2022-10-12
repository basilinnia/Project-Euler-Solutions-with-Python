"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def sieve_of_eratosthenes(limit):
    # we have a boolean array to storing "prime or not"s
    sieve = [True for i in range(limit + 1)]
    primes = []
    p = 2
    while p * p <= limit:
        # if prime[i] doesn't change it means this number is prime
        if sieve[p]:
            # update all multiples of our number
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
        p += 1

    # return sum of primes array
    for p in range(2, limit + 1):
        if sieve[p]:
            primes.append(p)

    return sum(primes)


n = 2000000
print(sieve_of_eratosthenes(n))

# answer : 142913828922
