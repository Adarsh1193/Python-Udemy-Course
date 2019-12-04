product = {"Laptop": 1500, "Desktop": 500, "Mobile": 1000, "Watch": 300, "Earphones": 200}
item = input("Enter the item")

if (item in product):
    print(product.get(item))
else:
    print('product not found')
