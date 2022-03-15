# Your code must return true or false (not 'true' and 'false') depending upon whether the given number is a
# Narcissistic number in base 10. This may be True and False in your language, e.g. PHP.
#
# Error checking for text strings or other invalid inputs is not required, only valid positive
# non-zero integers will be passed into the function.


# My version:
def narcissistic(n):
    return sum([int(i) ** len(str(n)) for i in str(n)]) == n


print(narcissistic(371))
