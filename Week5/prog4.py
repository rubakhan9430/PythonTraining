#Falling distance
#d = 1/2gt^2

def falling_distance(t):
    d = 0.5 *(9.8*(t**2))
    return d
for time in range(1,11):
    d = falling_distance(time)
    print('Time (seconds):', time,',','Distance (meters):', d)