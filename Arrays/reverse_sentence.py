# Reverce the words in the sentence
def revSentence(s):
    s.strip()
    rString = ''
    sWords = s.split(' ')
    for word in reversed(sWords):
        rString = rString + " " +  word.strip()
    return rString

s = "       This is the Best   "

def revSentence1(s):
    i = 0
    lenght = len(s)
    space = [' ']
    words = []
    while i < lenght:
        if s[i] not in space:
            wordstart = i
            while i < lenght and s[i] not in space:
                i += 1
            words.append(s[wordstart:i])
        i += 1
    return " ".join(reversed(words))
rs = revSentence1(s)
print(rs)

