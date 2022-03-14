# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.
#
# Example: create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

# My version:

def create_phone_number(n):
    my_string = str(n)
    sort = my_string[1:29:3]
    return f"({sort[:3]}) {sort[3:6]}-{sort[6:]}"


# Best Practices!!!
def best_practices(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(best_practices([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
