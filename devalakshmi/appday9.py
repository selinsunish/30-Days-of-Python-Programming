def copy_list(source_list):
    destination_list = []
    for item in source_list:
        destination_list.append(item)  
    return destination_list

source = [1, 2, 3, 4, 5]
destination = copy_list(source)
print("Source List:", source)
print("Destination List:", destination)
