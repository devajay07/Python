# needs to be done
n = int(input('Enter size of list: '))
a = list()
print('Enter the elements: ')
for x in range(0, n):
    x = int(input())
    a.append(x)
print(a)
for i in range(n-1):
    minIndex = i
    for j in range(i+1, n):
        if a[j] < a[minIndex]:
            minIndex = j

    a[i], a[minIndex] = a[minIndex], a[i]
print('Sorted List: ', a)
