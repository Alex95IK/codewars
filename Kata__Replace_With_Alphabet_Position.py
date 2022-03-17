# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.

# 'a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'l' 'm' 'n' 'o' 'p' 'q' 'r' 's' 't' 'u' 'v' 'w' 'x' 'y' 'z'
#  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26


# My version:
def alphabet_position(text):
    alphabet = list(map(chr, range(97, 123)))
    fin = [i + 1 for i in [alphabet.index(i) for i in text.lower() if i in alphabet]]
    return str(fin)[1:-1:].replace(',', '')


print(alphabet_position('Some text!'))


# Best Practices!!!
def best_practices(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
