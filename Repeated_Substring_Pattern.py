def repeatedSubstringPattern(s: str):
    N=len(s)
    def pattern(n):
        for i in (0,N-n,n):
            if s[i:n] != s[i+n:i+2*n]:
                return False
        return True
    for j in range(1,N//2+1):
        if pattern(j):
            return True
    return False
s='abcabcabcabc'
print(repeatedSubstringPattern(s))

# class Solution:
#     def repeatedSubstringPattern(self, s: str) -> bool:
#         l=len(s)
#         rep=''
#         for i in range(l//2):
#             rep += s[i]
#             if len(s) % len(rep) == 0:
#                 if rep * (len(s)//len(rep)) == s:
#                     return True
#         return False

