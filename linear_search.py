a = [1, 9, 5, 7, 15, 2, 20]
flag = 0
no = int(input('Enter the no. to be searched  '))
for x in a:
    if x == no:
        print('element found at index', a.index(x))
        flag = 1
        break
if flag != 1:
    print('element is not present')
