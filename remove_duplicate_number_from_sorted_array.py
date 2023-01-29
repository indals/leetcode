def removeDuplicates(nums):
    list1=[]
    for count, num in enumerate(nums):
        print(nums[count:],'--->',nums[count+1:])
        for i in range(nums.count(num)-1):
            nums.remove(num)
    return nums

print(removeDuplicates([1,1,2]))
