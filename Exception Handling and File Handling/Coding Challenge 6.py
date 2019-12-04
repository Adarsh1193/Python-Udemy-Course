# 1
file = open("Demo.txt", 'w')
file.write('This is a text')
file.close()

# 2
file = open("Demo.txt", 'r')
content = file.read()
print(content)
file.close()

# 3
file = open("Demo.txt", 'a')
file.write('This is the next line')
file.close()