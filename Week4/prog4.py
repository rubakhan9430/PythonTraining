speed = float(input('What is the speed of the vehicle in mph?'))
time = int(input('How many hours has it traveled?'))

for n in range(time + 1):
    distance = speed * n
    print(distance)