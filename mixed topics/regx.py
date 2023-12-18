import re
text="unicorn it have many charming elements "
pattern=r'\b[aeiou][a-z]*[^aeiou\W]\b'
match=re.findall(pattern,text)
print(match)