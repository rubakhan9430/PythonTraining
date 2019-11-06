item1 = float(input('Item 1 Price:'))
item2 = float(input('Item 2 Price:'))
item3 = float(input('Item 3 Price:'))
item4 = float(input('Item 4 Price:'))
item5 = float(input('Item 5 Price:'))

totalsale = item1 + item2 + item3 + item4 + item5
print('Total sale:', totalsale)
salestax = 6
print('Sales Tax %:', salestax)
totalsaleandtax = (totalsale * (salestax/100)) + totalsale
print('SubTotal:', totalsaleandtax)
