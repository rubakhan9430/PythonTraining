bugs = 0
L = [float(input('Monday:')), float(input('Tuesday:')),float(input('Wednesday:')),float(input('Thursday:')),float(input('Friday:')),float(input('Saturday:')),float(input('Sunday:'))]
for n in L:
    bugs = bugs + n
print('Total bugs:',bugs)