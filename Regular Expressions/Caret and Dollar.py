import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match found")
else:
    print('Match not found')