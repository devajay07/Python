# indexing in strings
a = 'Ajay Yadav'
for x in a:
    print(x)
print(a[5])

# strings are immutable:
# a[3] = 'r' it will give an error: 'str' object does not support item assignment
print(a[3])

# multiline strings:
a = ''' hello i am writing this 
   piece of code to showcase the use of multiline
   strings'''
print(a)

# negative indexing in python:
a = 'Ajay'
print(a[-1])  # gives the last character

# slicing in python:
a = 'AjayYadav'
print(a[:4])  # gives characters upto index 3
print(a[1:4])  # gives characters from index 1 to index 3
print(a[4:1:-1])  # gives characters from index 4 to index 2
print(a[:1:-1])  # gives characters from last index to index 2
# gives characters from last index to first index --> reversed string
print(a[::-1])
