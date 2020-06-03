#O(n) Complexity
def pair_sum(list1, k):
    #Edge Case 
    if len(list1) < 2:
        print("Please give the input list with lenght grater than 1")
    
    seen = set()
    output = set()
    for num in list1:
        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add((min(target, num), max(target, num)))
    print(output)
    if len(output) > 0:
        print("List is having pair of sum")
    else:
        print("List does not having pair of sum")


list1 = [1,4,5,3]
k = 6
pair_sum(list1, k)