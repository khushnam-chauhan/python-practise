# ^abc
# a-z
# A-Z
# 0-9

# Quantifiers:
# []?- ocuur 0 or 1
# []+- ocuur 1 or more time
# []*- ocuur 0 or more
# []{n}-occur n times
# []{n,}- occur n or more times
# []{y,z}- ocuurs atleast y times can occur less than z times


# regex metacharacters
# \d- [0-9]
# \D- [^0-9]
# \w- [a-z A-Z_0-9]
# \W- [^\w]


# 1) mobile number - start with 8 or 9 and total digit =10
# [89][0-9]{9}

# 2) first character uppercase, contains lower case alphabet only ione digit allowed in between
# [A-Z][a-z]*[0-9][a-z]*


# \b [aeiou][a-z]*[^aeiou\W]\b