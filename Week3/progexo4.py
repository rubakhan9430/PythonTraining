def autocost (loan,insurance,gas,oil,tires,maintenance):
    total = loan + insurance + gas + oil + tires + maintenance
    #annual = total * 12
    return (total)
def annualautocost(a):
    c = a * 12
    return (c)
loan = float(input('Loan payment:'))
insurance = float(input('Insurance:'))
gas = float(input('Gas:'))
oil = float(input('Oil:'))
tires = float(input('Tires:'))
maintenance = float(input('Maintenace:'))
d = autocost(loan,insurance,gas,oil,tires,maintenance)
print (d)
e = annualautocost(d)
print(e)


