"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,

then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example,
 342 (three hundred and forty-two) contains 23 letters and
 115 (one hundred and fifteen) contains 20 letters.
 The use of "and" when writing out numbers is in compliance with British usage.
"""

# from 1 to 10
# 3 3 5 4 3 5 5 4 3
# from 10 to 20
# 6 6 8 8 7 7 9 8 8
# şimdi kalanlar forty two gibi 10'un katlarından ve 1 in katlarından ilerleyecek
# 100 den sonrası içinse aynısının one, two three ... hundered and kısmı eklenecek

# from 1 to 9
one_digit_seq = [3, 3, 5, 4, 4, 3, 5, 5, 4]

# from 10 to 19
# I didn't use an array for them, i did it manually
# 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8 = 70
ten_to_twenty_sum = 70

# 20, 30, 40...80, 90
multiples_of_ten_seq = [6, 6, 5, 5, 5, 7, 6, 6]

# 1 to 99
one_to_ninety_nine_sum = sum(multiples_of_ten_seq) * 10 + 9 * sum(one_digit_seq) + ten_to_twenty_sum
# one_to_ninety_nine_sum = 854

# 100, 200, 300...800, 900
hundreds = 9 * 7

hundred_ands = 10 * (1000 - 100 - 9)

hundred_to_thousand_sum = hundreds + hundred_ands + (one_to_ninety_nine_sum * 9) + (100 * sum(one_digit_seq))

# add 1000 which equals eleven letters
print(hundred_to_thousand_sum + one_to_ninety_nine_sum + 11)

# this is the hard way of course but i wanted to explain all my steps with my variables
# answer: 21124
