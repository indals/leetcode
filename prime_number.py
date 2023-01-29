# prime_number=[]
# for i in range(100,200):
#     j=2
#     flag=0
#     while(True):
#         if i % j ==0:
#             flag=1
#             break
#         if j<i-10:
#                 j +=1
#         else:
#             break
#     if flag==0:
#         prime_number.append(i)
# print(prime_number)


# 2nd method



















print([num for num in range(100,200) if all(num%y!=0 for y in range(2,int(num/2-1)))])

