"""
The sum of the squares of the first ten natural numbers is,
                    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
                            3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


first_n = 100
range_num = first_n + 1

sum_of_squares = 0

for x in range(1, range_num):
    sum_of_squares += x ** 2

squares_of_sum = (range_num * (first_n//2))**2


print(squares_of_sum-sum_of_squares)