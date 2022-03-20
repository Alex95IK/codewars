# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits
# that occur more than once in the input string. The input string can be assumed to contain only alphabets
# (both uppercase and lowercase) and numeric digits.

def duplicate_count(text):
    x = text.lower()
    count = 0
    for i in x:
        if x.count(i) > 1:
            x = x.replace(i, '')
            count += 1
    return count


print(duplicate_count('1129gAwG2ykdG9aYdK'))


# Best Practices!!!
def best_practices(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])


print(best_practices('1129gAwG2ykdG9aYdK'))
