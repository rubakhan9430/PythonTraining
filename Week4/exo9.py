weight = float(input('Enter weight:'))

if weight <= 2:
    print('Shipping cost: $1.10')
elif weight > 2 and weight <= 6:
    print('Shipping cost: $2.20')
elif weight > 6 and weight <=10:
    print('Shipping cost: $3.70')
elif weight > 10:
    print('Shipping cost: $3.80')
else:
    print('Error')