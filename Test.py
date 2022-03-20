# a = [4, 3, 2, 1, 10, 14, -14]
# print(list(map(str, a)))
# # ['4', '3', '2', '1', '10', '14', '-14']


strn = "this is string example....wow!!!";


def best_practices(s):
    return len([i for i in set(s.lower()) if s.lower().count(i) > 1])


print(best_practices(strn))
