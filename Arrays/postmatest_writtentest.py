print("This Postmates coding test")

def alternatingSort(a):
    front = 1
    reverse = 1
    b = []
    #edge Cases 
    if len(a) == 1:
        b.append(a[0])
        return True
    i = 0
    while i < len(a):
        if i == 0:
            b.append(a[i])
            i += 1
        elif i % 2 != 0:
            b.append(a[-reverse])
            i += 1
            reverse += 1
            print(" I am inside odd")
        else:
            b.append(a[-front])
            i += 1
            front += 1
            print(" I am inside Even")
        c = b.sorted()
        print(c,b)
    return c == b

a = [6, 3, 5, 6, 4, 2]
print(alternatingSort(a))