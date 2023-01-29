def moveZeroes(nums):
    last=len(nums)-1
    flag=0
    for count,num in enumerate(nums):
        if num == 0 and count<=flag:
            for i in range(len(nums)-1,num+1,-1):
                flag=i
                if nums[i] == 0:
                    continue
                else:
                    tmp=[count]=nums[i]
                    nums[i]=nums[count]
                    nums[i]=tmp
    
    return nums

print(moveZeroes([0,1,0,3,12]))




        # dummy = cur = ListNode(0)
        # while l1 and l2:
        #     if l1.val < l2.val:
        #         cur.next = l1
        #         l1 = l1.next
        #     else:
        #         cur.next = l2
        #         l2 = l2.next
        #     cur = cur.next
        # cur.next = l1 or l2
        # return dummy.next



        serverless config credentials --provider aws --key AKIA2XSDSJXUQHMJX45N --secret m1Lf0xw0tZ4e0nlQJoKUvOS9YQv+9lvU4bFjSOr+