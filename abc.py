stalls[i-1]


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
				j++
			else break
arr=[]
subarr()