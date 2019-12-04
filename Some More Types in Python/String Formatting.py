numbers = [4, 5, 6]
newstring = "numbers:{0},{1},{2}".format(numbers[0],numbers[1],numbers[2])
print(newstring)

numbers = [12, 3, 2019]
newstring = "Date:{0}/{1}/{2}".format(numbers[0],numbers[1],numbers[2])
print(newstring)

a = "{x}/{y}".format(x=100, y=200)
print(a)