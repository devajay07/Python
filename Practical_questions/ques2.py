def commision():
    a = tuple()
    for ele in range(0, 4):
        a += int(input('enter this week earning ')),
    totalSalary = sum(a)
    if (totalSalary >= 8e4):
        print('excellent')
    elif (totalSalary >= 6e4):
        print('good')
    elif (totalSalary >= 4e4):
        print('average')
    else:
        print('work hard')
    if (totalSalary >= 5e4):
        print('commission: ', totalSalary*5/100)


commision()
