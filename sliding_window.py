

# Naivi solution
def Simple_sol(arr,k):
    res=0
    for i in range(0,len(arr)-2):
        ans=0
        for j in range(i,i+k):
            ans += arr[j]
            # print(j)/
        # print('stop')
        # print(ans)
        res=max(res,ans)
    return res
# arr=[5,-10,6,90,3]

# answer = Simple_sol(arr,2)
# print(answer)



# Efficient Solution

def sliding_window(arr,k):

    curr=0
    for i in range(0,k):
        curr += arr[i]
    res=curr
    for i in range(1,len(arr)+1-k):
        curr = curr-arr[i-1]
        curr += arr[i+k-1]
        res = max(curr,res)
    return res
arr=[5,-10,6,90,3]
result = sliding_window(arr,2)
print(result)












