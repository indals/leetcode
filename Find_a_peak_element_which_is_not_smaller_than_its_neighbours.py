def peak(arr):
    ans = []
    for i in range(len(arr)-2):
        first=arr[i]
        second = arr[i+1]
        third = arr[i+2]
        if second>first and second>third:
            # print(first, second, third)
            ans.append(second)
    print(ans)

arr=[10, 20, 15, 2, 23, 90, 67]
peak(arr)