# lst="python"

# for i in range(len(lst)):
# 	for j in range(i+1):
# 		print(lst[j],end="")
# 	print()
def subarr(arr,target):

	sum1=0
	j=0
	q=[]
	for i in range(len(arr)):
		sum1 += arr[i]
		q.append(arr[i])
		if sum1==target:
			return i
		while 1 and j<n-1:
			if sum1>target:
				sum1 = sum1-a[j]
				q.pop(0)
				j = j+1
			else:
				break
	print(q)
	arr=[1,4,20,3,10,5]
	subarr(arr,33)