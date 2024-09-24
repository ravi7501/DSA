#brute force approach  to find the two sum of array 
def sum_bruceforce(array,target):
    for i in range(0,len(array)-1):
        for j in range(1,len(array)):
            if (target==(array[i]+array[j])):
                return ("find_element",array[i],array[j])
            
array=[34,12,24,56,89,90,13]
print(sum_bruceforce(array,111))

#using hasing approach to find the two sum
# get the postion of element of two 
def two_sum(arr, target):
    mpp = {}
    for i in range(len(arr)):
        num = arr[i]
        more_needed = target - num
        if more_needed in mpp:
            return [mpp[more_needed], i]
        mpp[num] = i
    return [-1, -1]

print(two_sum(array,80))


#using two pointer approch

def two_pointer(arr,target):
    arr.sort()
    i=0
    j=len(arr)-1
    while(i<j):
       # print(i,j)
        if arr[i]+arr[j]==target:
            return (i,j)
        elif (arr[i]+arr[j])<target:
            i+=1
        else:
            j-=1
print(two_pointer(array,80))       

        