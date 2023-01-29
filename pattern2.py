   # 01234 
# 0*
# 1**
# 2* *
# 3*  *
# 4*****


n=int(input('Size of pattern: '))
for row in range(n):
	for col in range(n):
		if col==0 or row==(n-1) or row==col:
			print("*", end="")
		else:
			print(end=" ")
	print()	