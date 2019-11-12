def taxproperty(actual):
    assessment = actual * 0.6
    tax = assessment * 0.0064
    return assessment,tax

# def assessmentvalue (actual):
#     assessment = actual * 0.6
#     return assessment
# def propertytax(a):
#     tax = a * 0.0064
#     return tax
actual = float(input('Property value: $'))
# b = assessmentvalue(actual)
# print('Assessment value: $',b)
# c = propertytax(b)
# print('Property Tax: $',c)

d,e = taxproperty(actual)
print('Assessment: $',d)
print('Property Tax: $',e)