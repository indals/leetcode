def subarray(arr):
    n=len(arr)
    res=0
    for i in range(n):
        sum = 0
        count = 0
        for j in range(i,n):
            sum += arr[j]
            count +=1
            if sum==0:
                res=max(res,count)
    return res


arr=[15,-2,2,-8,1,7,10,23]
print(subarray(arr))
