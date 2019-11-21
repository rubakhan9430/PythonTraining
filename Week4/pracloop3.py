#write a program that runs a loop from 1 to 100
#display tic if a number is divisible by 5
#display tac if number divisible by 3
#display titac if a number divisible by 3 and 5

for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0: #put biggest condition first!
        print('titac')
    elif n % 5 == 0:
        print('tic')
    elif n % 3 == 0:
        print('tac')
    
    