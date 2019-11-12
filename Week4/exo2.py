length1 = float(input('Length1:'))
width1 = float(input('Width1:'))
Area1 = length1 * width1
length2 = float(input('Length2:'))
width2 = float(input('Width2:'))
Area2 = length2 * width2

if Area1 > Area2:
    print('Area of rectangle 1 is larger')
elif Area2 > Area1:
    print('Area of rectangle 2 is larger')
elif Area1 == Area2:
    print('Areas are the same')
else:
    print('Error')
