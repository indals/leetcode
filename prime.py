# prime.py
def prime():

	# start=100
	# for i in range(100,200):
	# 	flag=0
	# 	for j in range(2,int(start/2)):
	# 		# flag=0
	# 		if i%j==0:
	# 			flag=1
	# 	if flag==0:
	# 		print(i)
	for i in range(100,200):
		if all(i%j!=0 for j in range(2,int(i/2))):
			print(i)


prime()