file = open("Demo.txt", 'r')
content = file.read()
print(content)
file.close()

# Reading only the first line
file = open("Demo.txt", 'r')
content = file.readline()
print(content)
file.close()
