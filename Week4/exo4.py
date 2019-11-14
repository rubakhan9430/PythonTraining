month = float(input('Month in numerical form:'))
day = float(input('Day:'))
year = float(input('Year (2 digits):'))

if month * day == year:
    print('Date is magic')
else:
    print('Date is not magic')
