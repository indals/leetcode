def reverseVowels(s):
        i=0
        j=len(s)-1
        v=['a','e','i','o','u']
        s=list(s)
        print('Hello')
        while(i<=j):
            print(i,j)
            print(s[i],'------>',s[j])
            if s[i] in v and s[j] in v:
                s[i],s[j]=s[j],s[i]
                i +=1
                j -=1
            if s[i] in v and s[j] not in v:
                j -=1
            if s[i] not in v and s[j] in v:
                i +=1
            if s[i] not in v and s[j] not in v:
                i +=1
                j -=1
            # i +=1
            # j -=1
        res=''
        print(s)
s='leetcode'
reverseVowels(s)