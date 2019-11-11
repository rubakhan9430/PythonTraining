def calories (fat, carbohydrate):
    caloriesfat = fat * 9
    caloriescarb = carbohydrate * 4
    print('Calories from Fat:',caloriesfat)
    print('Calories from Carbs:',caloriescarb)
fat = float(input('Fat grams:'))
carbohydrate = float(input('Carb grams:'))
calories(fat,carbohydrate)


