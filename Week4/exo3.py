mass = float(input('Enter objects mass (kg):'))
weight = mass * 9.8

if weight > 1000:
    print('Object is too heavy')
elif weight < 10:
    print('Object is too light')
elif weight > 10 and weight < 1000:
    print('Object weight (newtons):',weight)
else:
    print('Error')