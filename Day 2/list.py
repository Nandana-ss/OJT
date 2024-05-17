# Check if an element exists in a list(16-05-2024)
clist = [10, 20, 30, 40, 50]
element_to_check = 30
if element_to_check in clist:
    print(f"{element_to_check} exists in the list.")
else:
    print(f"{element_to_check} does not exist in the list.")
    
# Sort a list in ascending order
slist = [5, 2, 8, 1, 3]
slist.sort()
print("Sorted list (ascending):", slist)

# Reverse a list
re_list = [1, 2, 3, 4, 5]
re_list.reverse()
print("Reversed list:", re_list)

#Find the sum of elements in a list
slist = [10, 20, 30, 40, 50]
total_sum = sum(slist)
print("Sum of elements:", total_sum)