def reverse_words(s):
    return ' '.join(reversed([i for i in s.split()]))


print(reverse_words('The greatest victory is that which requires no battle'))
