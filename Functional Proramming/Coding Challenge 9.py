def discount1(price):
    price = price - (price * 10) / 100
    return price

def discount2(newprice):
    newprice = newprice - (newprice * 5) / 100
    return newprice

SP = int(input('Enter the selling price'))

print(discount2(discount1(SP)))