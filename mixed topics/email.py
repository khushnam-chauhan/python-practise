import re

email = "example@email.com"

pattern = r'^([^@]+)@'
match = re.search(pattern, email)

if match:
    result = match.group(1)
    print(result)
