n=int(input('Enter number: '))
# 0 1 1 2 3 5 8 13 21 34 55 89 144
def fab(n):
	second_last=0
	last=1
	sum1=0
	for i in range(n):
		sum1=last+second_last
		second_last=last
		last=sum1
		print(i)
	print(sum1)

fab(n)