a = [1, 3, 4, 5, 6, 7, 8, 9, 20, 40]
no = int(input('Enter the no be to searched '))
lb = 0
ub = len(a)

while ub > lb:
    mid = int((lb+ub)/2)
    if a[mid] == no:
        print('element found at index ', mid)
        break
    elif a[mid] > no:
        ub = mid-1
    else:
        lb = mid+1
if lb >= ub:
    print("Element not found!")
