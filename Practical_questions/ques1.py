def triangle():
    side1 = int(input('Enter side 1 of the triangle'))
    side2 = int(input('Enter side 2 of the triangle'))
    side3 = int(input('Enter side 3 of the triangle'))
    perimeter = side1 + side2 + side3
    s = perimeter/2
    area = (s*(s-side1) * (s-side2) * (s-side3))**0.5
    return area, perimeter


print(triangle())
a = (2, 3, 4)
a += 10
print(a)
