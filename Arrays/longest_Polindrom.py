def get_longest_polindrom(string1):
    length = len(string1)
    poli = []
    for num in range(length, 0, -1): # num vales are starts from 4 to 3 to 2 to 1
        #print(num)
        #Found = False
        for s in  range(length-num+1):    # S values starts from 0 to 0,1 and 0,1,2, and 0,1,2,3
            target = string1[s:s+num]    ## string1[0:4] and [0:3],[1:4] and [0:2],[1,3],[2,4] and [0,1],[1,2],[2,3],[3,4]
            if target == target[::-1]:
                poli.append(string1[s:s+num])
               # Found = True
        #if Found:
        #    break
    return poli
            


string1 = "abba"
poli = get_longest_polindrom(string1)
print(poli)