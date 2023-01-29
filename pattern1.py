n=int(input("Enter A number"))
b=1
for i in range(1,n+1):
	for j in range(1,i+1):
		print(b, end=" ")
		b=b+1
	print()