# def palindrom(str,i,j):
#     if i>=j:
#         return True
#     # if str[i] != str[j]:
#     #     return False
#     return str[i]==str[j] and palindrom(str,i+1,j-1)
# str='kanak'
# print(palindrom(str,0,len(str)-1))


def arerotations(s1,s2) :
    if len(s1) != len(s2) :
        return -1
    else:
        temp = ''
        temp = s2+s1
        return temp.find(s2,1) !=1
        #     print('Yes')
        # else:
        #     print('No')
# s1 = "abcde"
# s2 = "abced"
# CDABABCD
s1 = "ABCD"
s2 = "CDAB"
print(arerotations(s1,s2))