lst=[1, -1, 3, 7, 8, 0, 2, 5, -6]
lst1=list(range(len(lst))) 
# print(lst1)
for num in lst:
    if num in lst1:
        lst1.remove(num)
print(lst1[0])