def factorial(x):
    if x == 1:
        return 1
    else:
        return x * (factorial(x-1))
    
a = int(input('Enter x'))
print(factorial(a))
