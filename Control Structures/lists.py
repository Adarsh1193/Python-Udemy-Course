names = ["Mike", "John", "Rob"]
print(names[2])

numbers = [1,2,3,4,5]
print(numbers[1])

abc = []
print(abc)

# list operations

number = [1,1,1,1,1]
number[2] = 5
print(number)

num = [2,2,2,2,2]
print(number + num + numbers)

print(numbers*3)

# to look for a particular item

fruits = ["apple", "mango", "peach"]
print("apple" in fruits)

# list functions

fruits = ["Apple", "Mango", "Peach", "Orange"]
fruits.append("Banana")
print(len(fruits))

fruits.insert(1, "Grapes")
print(fruits)
print(fruits.index("Peach"))