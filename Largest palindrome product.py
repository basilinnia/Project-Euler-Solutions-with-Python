"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

digits = 3
palindromes = []

for a in range(10**(digits-1), 10**digits):
    for b in range(10**(digits-1), 10**digits):
        temp = a * b
        if str(temp) == str(temp)[::-1]:
            palindromes.append(temp)

print(max(palindromes))

# answer: 906609
