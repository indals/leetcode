def subarray(arr,k):

    i,sum=0,0
    m,n=0
    lst=[]
    for j in arr:
        sum +=j
        lst.append(j)
        print(sum)
        while sum>k and i<len(arr)-1:
            sum = sum-arr[i]
            lst.pop(0)
            i +=1
        if sum==k:
            print('YEs')
            print(lst)

arr=[1, 4, 20, 3, 10, 5]
a=subarray(arr,33)
print(a)