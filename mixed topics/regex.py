import re
text="tht is always t"
pattern = r'^(.*)(.)\2$'
match = re.match(pattern, text)
if match:
        print("This is a match")
else:
        print("This is not a match")