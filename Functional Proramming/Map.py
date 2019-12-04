def add(x):
    return x + 2

newlist = [10, 20, 30, 40 ,50]

print(list(map(add,newlist)))

# Using lambdas
newlist = [10, 20, 30, 40 ,50]

print(list(map(lambda x: x + 2,newlist)))