budget = float(input('Enter budget for month:'))
x = 'y'
y = 0
while x == 'y':
    expenses = float(input('Enter Expense:')) 
    x = input('Enter y if you need to enter more expenses:')
    y = expenses + y
total = budget - y
print(total)