def append_item(my_list, item):
    my_list.append(item)
    print("Inside the function:", my_list)
original_list=[x for x in range (1,11)]
print("Before calling the function:", original_list)
append_item(original_list, 4)
print("After calling the function:", original_list)
