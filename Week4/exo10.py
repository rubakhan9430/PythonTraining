def bmi (weight, height):
    bmivalue = weight * 703/(height*height)
    return (bmivalue)
weight = float(input('Weight (lbs)'))
height = float(input('Height(inches)'))
a = bmi(weight,height)
print('BMI:',a)

if a < 18.5:
    print('You are underweight')
elif a >= 18.5 and a <= 25:
    print('You are at optimal weight')
elif a > 25:
    print('You are overweight')
else:
    print('Error')