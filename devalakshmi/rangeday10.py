numbers = [10, 20, 30, 40, 50]

reversed_indices = range(len(numbers)-1, -1, -1)
reversed_list = [numbers[i] for i in reversed_indices]
print(reversed_list)
