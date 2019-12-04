def square(x):
    return x * x

print(square(4))

# Working with lambda

result = (lambda x: x * x)(10)
print(result)

# lambdas are functions with no names and does not have a return statement
print((lambda x: x * x)(15))