#Find the largest continous sum from the given List/Array of elements 

def largestSum(list1):
    curr_sum = max_sum = list1[0]
    for num in list1[1:]:
        curr_sum = max(curr_sum + num, curr_sum)
        max_sum = max(curr_sum, max_sum)

    return max_sum

list1 = [1,2,-1,3,4,10,10,-10,-1]
print(largestSum(list1))