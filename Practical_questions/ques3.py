def series():
    result = []
    a = 0
    b = 1
    n = int(input('Enter the value of n '))
    i = 1
    while i < n:
        sum = a+b
        a = b
        b = sum
        i += 1
    result.append(sum)


series()
