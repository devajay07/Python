# needs to be done
n = int(input('Enter size of list: '))
a = list()
print('Enter the elements: ')
for x in range(0, n):
    x = int(input())
    a.append(x)
for i in range(0, n-1):
    for j in range(n-1):
        if (a[j] > a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
print('Sorted List: ', a)
