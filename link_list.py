# link_list.py
class Node:
	def __init__(self,data=None, next=None):
		self.data=data
		self.next=next
		# print(self.data)
class LinkedList:
	def __init__(self):
		self.head=None

	def InsertAtEnd(self,data):
		temp=Node(data)
		if self.head is None:
			self.head=temp
			# print('Reach')
		else:
			itr=self.head
			while(itr.next!=None):
				itr=itr.next
			itr.next=temp
	def print(self):
		if self.head is None:
			print("LinkedList is Empty")
		else:
			itr=self.head
			while(itr.next!=None):
				print(itr.data,'----->',end='')
				itr=itr.next
			print(itr.data)
	def InsertAtBegining(self,data):
		temp=Node(data,self.head)
		self.head=temp
		# if self.head is None:
		# 	self.head=temp
		# else:
		# 	temp=self.head
		# 	self.head=temp
		# 	print('Reach')

	def get_length(self):
		itr=self.head
		count=0
		while(itr.next!=None):
			count += 1
			itr=itr.next
		return count
	def InsertAt(self,data,at):
		
		if at<0 or at>self.get_length():
			raise Exception("Invalid Index")
		if at == 0:
			InsertAtBegining(data)
		else:
			count=0
			itr=self.head
			while(count!=at):
				if count == at-1:
					node=Node(data)
					node.next=itr.next
					itr.next=node
					break
				count+=1
				itr=itr.next
	def delete_from_begining(self):
		self.head=self.head.next
	def delete_from_end(self):
		itr=self.head
		while(itr.next.next!=None):
			itr=itr.next
		itr.next=None




if __name__=='__main__':
	obj=LinkedList()
	obj.InsertAtEnd(2)
	obj.InsertAtEnd(3)
	obj.InsertAtEnd(4)
	obj.InsertAtEnd(5)
	obj.InsertAtEnd(6)
	obj.InsertAtEnd(7)
	obj.print()
	obj.InsertAtBegining(10)
	print('LinkedList length is: {}'.format(obj.get_length()))
	obj.InsertAt(15,4)
	# obj.get_length()
	print('LinkedList length is: {}'.format(obj.get_length()))
	obj.print()
	obj.delete_from_begining()
	obj.delete_from_begining()
	obj.delete_from_end()
	obj.print()