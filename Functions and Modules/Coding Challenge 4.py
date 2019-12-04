def BMI(height, weight):
    return weight / height ** 2

w = float(input("Enter the weight"))
h = float(input("Enter the height"))

result = BMI(h, w)
print(result)