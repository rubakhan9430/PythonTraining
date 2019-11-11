def seats(a,b,c):
    classA = a * 15
    classB = b * 12
    classC = c * 9
    totalcost = classA + classB + classC
    return(totalcost)
a = float(input('Class A tickets:'))
b = float(input('Class B tickets:'))
c = float(input('Class C tickets:'))
e = seats(a,b,c)
print(e)

