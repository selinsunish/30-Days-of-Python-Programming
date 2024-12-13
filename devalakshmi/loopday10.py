def sort_descending(lst):
    
    n = len(lst)
    
    for i in range(n):
        
        for j in range(0, n-i-1):
            
            if lst[j] < lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    
    return lst

my_list = [34, 2, 12, 56, 7, 89, 3]

sorted_list = sort_descending(my_list)

print("List sorted in descending order:", sorted_list)

