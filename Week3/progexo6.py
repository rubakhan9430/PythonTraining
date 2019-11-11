def bmi (weight, height):
    bmivalue = weight * 703/(height*height)
    return (bmivalue)
weight = float(input('Weight (lbs)'))
height = float(input('Height(inches)'))
a = bmi(weight,height)
print('BMI:',a)