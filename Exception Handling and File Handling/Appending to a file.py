file = open("Demo.txt", 'w')
file.write("This is the text written to the file")
file.close()

file = open("Demo.txt", 'r')
content = file.read()
print(content)
file.close()

file = open("Demo.txt", 'a')
file.write("This is the next line")
file.close()