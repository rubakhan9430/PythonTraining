bugs = 0
L = [float(input('Monday:')), float(input('Tuesday:')),float(input('Wednesday:')),float(input('Thursday:')),float(input('Friday:')),float(input('Saturday:')),float(input('Sunday:'))]
for n in L:
    bugs = bugs + n
print('Total bugs:',bugs)


# total = 0
# for day in range(7):
#     nbugs = int(float(input('How many bugs did you collect today?: ')))
#     print('You have collected today' + str(nbugs))
#     total = total + nbugs
# print('Total bugs:',total)