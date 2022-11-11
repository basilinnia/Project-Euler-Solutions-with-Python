"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def factorial(num):
    if num == 1:
        return num
    else:
        return factorial(num - 1) * num


number = 100
result = 0


def zeroes(num):
    myzero = 0
    while num > 5:
        num //= 5
        myzero += num
    return myzero


zero = zeroes(number) * -1

fact = str(factorial(number))[:zero]
result = sum(int(i) for i in fact)
print(result)

# answer: 648
