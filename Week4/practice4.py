def sum (tax,interest,amount):
    total = amount*tax + amount
    total = total*interest + total
    return total

def Hello():
    print('Hello Everyone!')

if __name__ == "__main__":
    Hello()
    a = float(input('Enter amount to borrow:'))
    b = 0.2
    c = float(input('Interest:'))

    d = sum(b,c,a)
    print('Total amount:',d)
