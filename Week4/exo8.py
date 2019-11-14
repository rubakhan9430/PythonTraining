numberpackages = float(input('Packages:'))
packages = 99
totalpack = numberpackages * packages
discount1 = totalpack * (20/100)
discount2 = totalpack * (30/100)
discount3 = totalpack * (40/100)
discount4 = totalpack * (50/100)
price1 = totalpack - discount1
price2 = totalpack - discount2
price3 = totalpack - discount3
price4 = totalpack - discount4

if numberpackages >=10 and numberpackages <=19:
    print('Discount:',discount1)
    print('Price:',price1)
elif numberpackages >=20 and numberpackages <=49:
    print('Discount:',discount2)
    print('Price:',price2)
elif numberpackages >=50 and numberpackages <=99:
    print('Discount:',discount3)
    print('Price:',price3)
elif numberpackages >=100:
    print('Discount:',discount4)
    print('Price:',price4)
else:
    print('Error')