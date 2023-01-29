# 

Input: nums = duplicate([1,3,4,2,2])
Output: 2
def duplicate(arr):
	n = len(arr)
	arr = list(arr)
	i = 0
	while(i<n):
		if arr[i] != (i+1):
			corrct_pos=arr[i]-1
			if arr[i] != arr[corrct_pos]:
				arr[i],arr[corrct_pos]=arr[corrct_pos],arr[i]
			else:
				i +=1
		else:
			i = i+1
	return arr

	helper


	while root.next:

if (not root):
        return INT_MAX

    """ If root.data is equal to key """
    if (root.data == key):
        return root.data

    """ If root.data is greater than the key """
    if (root.data > key):
        return floor(root.left, key)

    """ Else, the floor may lie in right subtree 
    or may be equal to the root"""
    floorValue = floor(root.right, key)
    return floorValue if (floorValue <= key) else root.data