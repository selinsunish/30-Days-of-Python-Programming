# Python program to sort a list in ascending order

def sort_ascending(lst):
    lst.sort()  
    return lst

my_list = [5, 2, 9, 1, 5, 6]
ascending_sorted_list = sort_ascending(my_list)

print("List sorted in ascending order:", ascending_sorted_list)

# Python program to sort a list in descending order

def sort_descending(lst):
    lst.sort(reverse=True)  
    return lst
my_list = [5, 2, 9, 1, 5, 6]
descending_sorted_list = sort_descending(my_list)

print("List sorted in descending order:", descending_sorted_list)
