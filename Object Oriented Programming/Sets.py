# Can only have unique elements
"""
numbers = {1, 2, 3, 4, 4, 5, 6}
print(numbers)

print(5 in numbers)

numbers.add(9)
print(numbers)

numbers.remove(4)
print(numbers)
"""

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# Union of the sets
print(setA | setB)

# Intersection of the sets
print(setA & setB)

# Difference of the sets
print(setA - setB)