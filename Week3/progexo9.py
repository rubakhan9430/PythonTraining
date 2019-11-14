def paintjob(feet):
    gallon = feet/115
    labor = gallon * 8
    laborcost = labor * 20
    return gallon,labor,laborcost
feet = float(input('Square feet:'))
a,b,c = paintjob(feet)
print('Total cost:',c)
print('Gallons:',a)
print('Labor:',b)

