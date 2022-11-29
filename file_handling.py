# reading from a file
f = open('/Users/moksh/Documents/College/read.txt', 'r')
print(f.read())
f.close()  # free all the resources

# recommended way:
with open('/Users/moksh/Documents/College/read.txt', 'r') as f:
    f.read()

# append to a file:

with open('/Users/moksh/Documents/College/read.txt', 'a') as f:
    print(f.write('ok now tata good byee'))
    print(f.write('ok now tata good byee'))

# write to a file:

with open('/Users/moksh/Documents/College/read.txt', 'w') as f:
    print(f.write('ok now tata good byee'))
    print(f.write('ok now tata good byee'))
