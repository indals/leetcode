def fun(n):

    a=0
    b=1
    c=0
    # sum=0
    for i in range(n):
        a=b
        b=c
        c = b+a
        # print(c)
        # a = b
    return c

# print(fun(10))

def rec(n):
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    return rec(n-2)+rec(n-1)

print(rec(6))

