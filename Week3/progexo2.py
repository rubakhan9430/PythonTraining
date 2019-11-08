#purchase = float(input('Total purchase:'))
#statesalestax = purchase * 0.04
#countysalestax = purchase * 0.02
#totaltax = statesalestax + countysalestax
#totalamount = purchase + totaltax

#print('Total purchase:', purchase)
#print('State sales tax:', statesalestax)
#print('County sales tax:', countysalestax)
#print('Total tax:', totaltax)
#print('Total amount due:', totalamount)

def statesalestax(purchase):
    a = purchase * 0.04
    b = purchase * 0.02
    c = a + b
    d = c + purchase
    print(d)
e = float(input('Purchase:'))
statesalestax(e)
