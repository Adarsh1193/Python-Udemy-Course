def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Divide by zero exception')
        
x = int(input('Enter the first number'))
y = int(input('Enter the second number'))

result = divide(x,y)
print(result)
