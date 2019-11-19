days = int(input('Days:'))
#salary = 0
for pennies in range(days+1):
    salary = pennies * 2
    dollar = salary/100
    print('$',dollar)
print('Total Salary: $',dollar)