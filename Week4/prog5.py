total = 0
for years in range(int(input('Years:'))):
    for months in range (12):
        rain = float(input('Inches of rain:'))
        total = rain + total
average = total/months
print('Years:',years+1,'Months:',months+1,'Rainfall total:',total,'Average Rainfall:',average)
