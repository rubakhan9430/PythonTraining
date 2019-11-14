pennies = float(input('Enter Pennies:'))
nickels = float(input('Enter Nickels:'))
dimes = float(input('Enter Dimes:'))
quarters = float(input('Enter Quarters:'))
total = pennies + nickels + dimes + quarters

if total == 100:
    print('Congratulations!')
elif total < 100:
    print('Amount is less than a dollar')
elif total > 100:
    print('Amount is more than a dollar')
else:
    print('Error')
