def numbers (a):
    result = number % 2
    if result == 0:
        print('Even number')
    else:
        print('Odd number')
number = int(input('Enter number:'))
numbers(number)
    

# Another way of doing it
# def numbers (number = int(input('Enter number:'))):
#     result = number % 2
#     if result == 0:
#         print('Even number')
#     else:
#         print('Odd number')
# numbers()

# Another way of doing it
# def numbers (number = int(input('Enter number:'))):
#     result = number % 2
#     if result == 0:
#         return Even number
#     else:
#         return Odd number
# y = numbers(x)
# print(y)