def find_multiples_of_5(lst):
    multiples_of_5 = [num for num in lst if num % 5 == 0]
    return multiples_of_5

numbers = [2, 4, 5, 8, 10, 30, 15]

result = find_multiples_of_5(numbers)
print("Multiples of 5 in the list:", result)
