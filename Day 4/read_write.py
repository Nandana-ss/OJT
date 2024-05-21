# Write a Python program to Read/Write to a File
dummy = open("dummy.txt","w+")
dummy.write("Hello world")
dummy.seek(0)
content= dummy.readlines()
print(content)
dummy.close()

