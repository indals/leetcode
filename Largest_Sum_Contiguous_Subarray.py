
def subarray(arr):
    maxsubarray_so_for=0
    curr_sum=0
    k,l=0,0
    for i in range(len(arr)):
        if curr_sum > maxsubarray_so_for:
            l=i
            maxsubarray_so_for=curr_sum
        if curr_sum<0:
            curr_sum=0
            k=i
        curr_sum +=arr[i]
    print('from {} to {} and maximum sum is {}'.format(k,l-1,maxsubarray_so_for))
arr=[-2, -3, 4, -1, -2, 1, 5, -3]
subarray(arr)