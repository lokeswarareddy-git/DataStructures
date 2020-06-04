#Find wearther string is having Uniq Charectors are not 
from collections import Counter
def isHavingUniq(s):
    C = Counter(s)
    for key in C:
        if C[key] != 1:
            return False
    return True
s= 'abcde'
print(isHavingUniq(s))


def uni_Char2(s):
    return len(set(s)) == len(s)

s= 'abcdaf'
print(uni_Char2(s))

def uniq_char3(s):
    char = set()
    for c in s:
        if c in char:
            return False 
        else:
            char.add(c)
    return True

s= 'abcdf'
print(uniq_char3(s))
