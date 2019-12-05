import re

pattern = r"eggs"

if re.match(pattern, "beggsbacon"):
    print('Match found')
else:
    print('No match found')

if re.search(pattern, "baconeggsbacon"):
    print("Match found")
else:
    print("Match not found")

print(re.findall(pattern, "baconeggseggsbacon"))
