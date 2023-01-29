def RainWaterTrap(arr,n):

	Lmaxblock = [0]*n
	Rmaxblock = [0]*n
	Lmaxblock[0] = arr[0]
	for i in range(1,n):
		Lmaxblock[i]=max(Lmaxblock[i-1],arr[i])
	Rmaxblock[n-1] = arr[n-1]
	for i in range(n-2,-1,-1):
		Rmaxblock[i]=max(Rmaxblock[i+1],arr[i])
	result = 0
	for i in range(n): 
		result += min(Lmaxblock[i], Rmaxblock[i])-arr[i]
	return result

list1 = list(map(int,input('Enter array value in a line').split()))
n = len(list1)
answer = RainWaterTrap(list1,n)
print(f'We can trap only {answer} unit water')


3
2
3
2 0
1 0
0 1
2
4 2 1 0 1 1
4 2 1 0 2 1


3
3
2
0 0 1
1 0 0
1 0 0
2
5 1 0 0 2 2
5 1 1 2 2 2

3
3
4
0 1 1
1 2 3
0 2 1
2
0 1 0 0 2 2
2 2 1 1 2 2

And Your Code's output is:

6 0


Its Correct output is:

6 2



count=0
flag= 0 
for i in arr:
	if i%2==0:
		count +=1
		flag = 1



def solve(n,k,stalls):








n,k=list(map(int, input().split()))
stalls = list(map(int,input().split()))
res=solve(n,k,stalls)
print(res)

def fun(func):
	def exe():
		print('Going to run')
		func()
		print('Done')
	return exe

@fun
def main():
	print('This will be execute')
main()


