import re

pattern = r"bread(eggs)*bread"

if re.match(pattern, "breadeggseggseggsbread"):
    print('Match found')
else:
    print('Match not found')