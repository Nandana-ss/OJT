# Write a Python program to count the number of vowels in a string.(16-05-2024)
word=input("enter the word:")
split_word=word.upper()
count=0
for i in split_word:
    if(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        count+=1
print(count)
