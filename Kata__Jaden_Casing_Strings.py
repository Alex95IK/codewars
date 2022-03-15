# Your task is to convert strings to how they would be written by Jaden Smith.
# The strings are actual quotes from Jaden Smith,
# but they are not capitalized in the same way he originally typed them.

import re


def to_jaden_case(string):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo:
                  mo.group(0)[0].upper() +
                  mo.group(0)[1:].lower(), string)


print(to_jaden_case("Let's go to Party"))


# Best Practices:
def to_jaden_case(string):
    return " ".join(w.capitalize() for w in string.split())
