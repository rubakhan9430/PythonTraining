seconds = float(input('Enter seconds:'))
secondsmin = seconds/60
secondshour = seconds/3600
secondsday = seconds/86400
if seconds >= 60 and seconds < 3600:
    print(secondsmin)
elif seconds >= 3600 and seconds < 86400:
    print(secondshour)
elif seconds >= 86400:
    print(secondsday)
else:
    print('Error')
