
def subarray_sum_with_given_sum(arr,target):
    for i in range(len(arr)):
        curr_sum=0
        for j in range(i,len(arr)):
            # print(curr_sum)
            curr_sum += arr[j]
            print(arr[j],end=' ')
            if curr_sum ==target:
                return True
        print(curr_sum)
    return False

arr=[3,2,0,4,7]
ans=subarray_sum_with_given_sum(arr,5)
print(ans)