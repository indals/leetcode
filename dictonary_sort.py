dict1={575: "Apple", 342: "Manggo", 452: "Banana", 56: "Grapes"}

keys=sorted(dict1.keys(), reverse=True)
dict2=dict()
for i in keys:
    dict2[i]=dict1[i]
print(dict2)
