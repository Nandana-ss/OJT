# INDEX 
# This method returns the index of the specified elements. It takes one argument. If the element specified is not present, it generates an error.
l=[7,4,2,6,9,15]
a=l.index(9)
print(a)

# APPEND
# This method is used for appending and adding elements to the List. It is used to add elements to the last position of List. It takes only one argument so it can append only one element at a time.
l=[2,4,6,7,8]
l.append(12)
print(l)

# EXTEND
# If we want to append several objects contained in a list, we use Extend(). This method adds multiple items but it should be in the form of a list.
l1=[3,6,2]
l2=[9,7,1]
l1.extend(l2)
print(l1)

# INSERT 
# The Insert method is used to insert an element into a list. It accepts two parameters, 
l=[2,4,6]
l.insert(2,14)
print(l)

# POP
# This method is used to delete an element from the list from the end. It takes an index as an optional parameter. That is if you don't pass any argument then it will remove the item from the end of the list;otherwise, it will remove the item from the specified position.
l=[2,3,8,7,9,6,5]
l.pop()
print(l)
l.pop(3)
print(l)

# REMOVE 
# This method is used to delete an element from the List. However, it is different from the pop() method. Instead of deleting an element from the index, it will delete an element as per the argument. That is, we can pass an element as an argument to be deleted.
l=[2,3,8,7,9,6,5]
l.remove(3)
print(l)

# CLEAR
# This method is used to clear the whole list, i.e., it removes all the items from the list. 
l=[2,3,8,7,9,6,5]
l.reverse()
print(l)

# SORT
# This method is used to sort a list. By default, the list is sorted in ascending order. We can also sort a list in descending order, bypassing "reverse=True" as an argument in sort().
l=[2,3,4,8,7,9,6,5]
l.sort()
print(l)
l.sort(reverse=True)
print(l)

# COUNT 
# This method will return the number of times the element occurs within a specified list. It takes one argument, as an element to be counted
l=[2,3,4,8,7,9,6,5]
l.count(3)
print(l)