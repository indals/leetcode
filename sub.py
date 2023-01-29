def subarr(arr,target):

    sum1=0
    j=0
    q=[]
    n=len(arr)
    for i in range(len(arr)):      
        if sum1==target:
            return q
        sum1 += arr[i]
        q.append(arr[i])
        while True:
            print(sum1)
            if sum1>target:
                sum1 = sum1-arr[j]
                print(arr[j])
                q.pop(0)
                j = j+1
            else: break

    print(q)
arr=[15,2,4,8,9,5,10,3]
print(subarr(arr,23))