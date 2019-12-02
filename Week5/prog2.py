import math
import random
a = random.randint(0,200)
b = random.randint(0,200)
print (a, '+', b)
c = a + b
d = float(input('Answer:'))

if c == d:
    print('Congratulations!')
else:
    print('Wrong answer!', 'Correct Answer is',c)
