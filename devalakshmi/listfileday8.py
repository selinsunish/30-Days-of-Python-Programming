def sum_of_elements(lst):
    total = 0
    for num in lst:
        total += num
    return total
numbers = [12, 15, 3, 10]
result = sum_of_elements(numbers)
print("Sum of all elements:", result)
