"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
 there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""


def factorial(num):
    if num == 1:
        return num
    else:
        return factorial(num - 1) * num


def solution(horizontal_grid, vertical_grid):
    routes = horizontal_grid + vertical_grid
    return factorial(routes)//(factorial(horizontal_grid)*factorial(vertical_grid))


print(solution(20, 20))

