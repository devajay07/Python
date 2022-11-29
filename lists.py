# list is what we know as array in other languages.
a = [1, 2, 3, 3, 'Ajay']
for x in a:
    print(x, end=", ")

# list methods:
print(a.index(3))  # gives the index of element
print(a.count(3))  # gives the frequency of element
a.remove(3)  # removes the elment
print(a)
a.clear()  # clears the list
print(a)

# list functions:
del (a)  # will delete the list from the memory
# print(a) --> it will give error as a is no longer defined

# list comprehenision: shorter syntax to create lists:
# create a list with odd lements upto 10
a = [x for x in range(10) if x % 2 != 0]
print(a)
