#  Find the missing element from the list2 which is suffeled list  from list1 and  got one elemenet removed 
#from the list2
# Solution 1:

def finder(list1, list2):
    list1.sort()
    list2.sort()

    #edge Cases
    if len(list1) != len(list2) -1 :
        print("List 2 is missing more than one elelement from list1")

    list3 = list(set(list1) - set(list2))
    print( "missing element from list1 and list2:", list3)

list1 = [1,2,5,7,8,6,9]
list2 = [1,2,8,6,5,9]
#finder(list1, list2)

#Solution 2:

def finder2(list1, list2):
    #list1.sort()
    #list2.sort()

    # Edge Cases 
    if len(list1) != len(list2) + 1 :
        print("List2 is missing more than one element from list1 so please check the inputs")
    
    for num in list1:
        if num  not in list2:
            return num
    
list1 = [1,2,5,7,8,6,9]
list2 = [1,2,8,6,5,9]
missing_num = finder2(list1, list2)
print ("Missing Number :", missing_num)


# Solution 3

def finder3(list1, list2):
    list1.sort()
    list2.sort()
    for i, num in enumerate(list1):
        if list1[i] != list2[i]:
            return num


list1 = [1,2,5,7,8,6,9]
list2 = [1,2,8,6,5,9]
missing_num = finder3(list1, list2)
print ("Missing Number from finder3 method :", missing_num)



# Solution 4
import collections
def finder4(list1, list2):
    d = collections.defaultdict(int)
    for num in list2:
        d[num] += 1
        print(d)
    for num in list1:
        if d[num] == 0:
            return num
        else:
            return list1[-1]

list1 = [1,2,5,7,8,6,9]
list2 = [1,2,8,6,5,9]
missing_num = finder4(list1, list2)
print ("Missing Number from finder3 method :", missing_num)

