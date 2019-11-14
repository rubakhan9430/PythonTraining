books = float(input('Books purcahsed:'))

if books == 0:
    print('Awards: 0')
elif books == 1:
    print('Awards: 5')
elif books == 2:
    print('Awards: 15')
elif books == 3:
    print('Awards: 30')
elif books >= 4:
    print('Awards: 60')
else:
    print('Error')
