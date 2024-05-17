# Check if a key exists in a dictionary
kdict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
key_to_check = 'city'
if key_to_check in kdict:
    print(f"{key_to_check} exists in the dictionary.")
else:
    print(f"{key_to_check} does not exist in the dictionary.")

# Remove a key-value pair from a dictionary.
rdict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
del rdict['age']
print("Updated dictionary:", rdict)

# Merge two dictionaries
dict1 = {'name': 'Alice', 'age': 30}
dict2 = {'city': 'New York', 'country': 'USA'}
merged_dict = {**dict1, **dict2}
print("Merged dictionary:", merged_dict)

# Find the length of a dictionary
fdict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
length = len(fdict)
print("Length of the dictionary:", length)

# Get a list of keys or values from a dictionary
gdict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
keys_list = list(gdict.keys())
print("Keys:", keys_list)
values_list = list(gdict.values())
print("Values:", values_list)