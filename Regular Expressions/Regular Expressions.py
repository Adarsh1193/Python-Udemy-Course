import re

pattern = r"eggs"

if re.match(pattern, "beggsbacon"):
    print('Match found')
else:
    print('No match found')