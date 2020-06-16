from collections import Counter

def strCompress1(s):
    c = Counter(s)
    compressed_String = ''
    for key in c:
        compressed_String = compressed_String + key + str(c[key])
    return compressed_String
s = 'AAAABBBBBCCCC'
print(strCompress1(s))

def strCompress2(s):
    r = ""
    count = 1
    i = 1
    length = len(s)

    # Foloowing are Edge Cases
    if length == 0:
        return ""
    if length == 1:
        return s + "1"
    ## Above are Edge Cases 
    
    while i < length :
        if s[i] == s[i-1]:
            count += 1
        else: 
            r = r + s[i-1] + str(count)
            count = 1
        i += 1
    r = r + s[i-1] + str(count)
    return(r)

s = 'AAAABBBBBCCCC'
print(strCompress2(s))