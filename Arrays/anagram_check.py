#Easy Solution 
def anagram1(s1, s2):
    s1 = s1.replace(' ' , '').lower()  #O(n)
    s2 = s2.replace(' ' , '').lower()  #O(n)
    return sorted(s1) == sorted(s2)

# Solution with some coding involded 

def anagram2(s1, s2):
    s1 = s1.replace(' ', '').lower()      #O(n)
    s2 = s2.replace(' ', '').lower()      #O(n)

    #Edge Case 
    if len(s1) != len(s2):     #O(1)
        return False
    ##
    counter = {}

    for letter in s1:      #O(n)
        if letter in counter:
            counter[letter] += 1
        else:
            counter[letter] = 1

    for letter in s2:       #O(n)
        if letter in counter:
            counter[letter] -= 1
        else:
            counter[letter] == 1
    for k in counter:     #O(n)
        if counter[k] != 0:
            return False

    return True 
    ### Pythonic way of solution 
from collections import Counter
def anagram3(s1, s2):
    s1 = s1.replace(' ', '').lower()  #O(n)
    s2 = s2.replace(' ', '').lower()  #O(n)

    d1 = Counter(s1)   #O(n)
    d2 = Counter(s2)   #O(n)
    if len(d1) != len(d2):
        return False
    else:
        for letter in d1:   #O(n)
            if d1[letter] == d2[letter]:
                pass
            else:
                return False
    return True


s1 = input("Enter the string1: ")
s2 = input("Enter the String2: ")
print("Is S1 and S2 are Anagram? : ",anagram3(s1, s2))
