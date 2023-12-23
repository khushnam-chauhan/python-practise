import re

email = "example@email.com"
#'^([^@]+)@'
pattern = r'^(.+)@'
match = re.search(pattern, email)

print(match.group(1))