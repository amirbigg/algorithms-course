"""
isomorphic strings

    foo bar => False
    foo bee => True


    { f:b, o:a }
    (b, a, r)

"""

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    dict_values = {}
    set_values = set()

    for i in range(len(t)):
        if s[i] not in dict_values:
            if t[i] in set_values:
                return False
            dict_values[s[i]] = t[i]
            set_values.add(t[i])
        else:
            if dict_values[s[i]] != t[i]:
                return False

    return True


print(is_isomorphic('paper', 'title'))
