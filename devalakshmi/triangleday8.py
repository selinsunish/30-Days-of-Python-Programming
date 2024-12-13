def print_triangle(lst):
    for i in range(1, len(lst) + 1):
         print(' '.join(map(str, lst[:i])))
numbers = [2, 4, 5, 8, 10, 30, 15]

print_triangle(numbers)
