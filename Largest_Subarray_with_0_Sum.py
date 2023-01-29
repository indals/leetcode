def subarray(arr):
    sum=0
    map1={}
    map1[0]=-1
    res=0
    count = 0
    for i in range(len(arr)):
        sum += arr[i]
        if map1.get(sum) is not None:
            count = i-map1[sum]
        else:
             map1[sum]=i
        res=max(res,count)
    print(map1)
    return res



arr=[15,-2,2,-8,1,7,10,23]
print(subarray(arr))
