#Test Average and Grade
def calc_average(a,b,c,d,e):
    average = (a+b+c+d+e)/5
    print('Average:',average)
def determine_grade(a):
    if a >=90 and a <= 100:
        print('A')
    elif a >= 80 and a <= 89:
        print('B')
    elif a >= 70 and a <= 79:
        print('C')
    elif a >= 60 and a <= 69:
        print('D')
    else:
        print('F')

if __name__ == '__main__':
    #a = float(input('Enter Grade:'))
    #determine_grade(a)

    grade1 = float(input('Grade:'))
    determine_grade(grade1)
    grade2 = float(input('Grade:'))
    determine_grade(grade2)
    grade3 = float(input('Grade:'))
    determine_grade(grade3)
    grade4 = float(input('Grade:'))
    determine_grade(grade4)
    grade5 = float(input('Grade:'))
    determine_grade(grade5)
    calc_average(grade1,grade2,grade3,grade4,grade5)


