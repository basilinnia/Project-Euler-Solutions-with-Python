"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def is_prime(nums):
    for i in range(2, nums):
        if nums % i == 0:
            return False
    return True


prime_numbers = [2]


# This isn't the optimal solution but I wanted to see the array of the prime numbers
def nd_prime(nd_num):
    n = 2
    while len(prime_numbers) < nd_num:
        n += 1
        if is_prime(n):
            prime_numbers.append(n)


nd_prime(10001)
print(prime_numbers[-1])

# answer: 104743
