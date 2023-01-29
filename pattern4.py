n=int(input('Enter a number'))
for col in range(n):
	for row in range(n):
		if col==row or col==0 or row==(n-1):
			print('*', end="")
		else:
			print(end=" ")
	print()