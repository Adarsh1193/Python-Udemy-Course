import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "AP1"):
    print('Match found')
else:
    print('Match not found')