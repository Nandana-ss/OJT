# Write a Python program that renames a file named ‘old_name.txt to’ ‘new_name.txt’.
import os
old_name = "old_name.txt"
new_name = "new_name.txt"
os.rename(old_name, new_name)