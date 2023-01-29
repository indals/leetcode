class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head=None

    def Insert_at_end(self,data):
        
        if self.head==None:
            self.head=Node(data)
        else:
            tmp = self.head

            while tmp.next:
                tmp = tmp.next
            tmp.next=Node(data)
    def Insert_at_start(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            tmp = Node(data)
            tmp.next=self.head
            self.head = tmp
    def reverse(self):
        if self.head is None:
            print('There is no emement in linkedlist')
        else:
            tmp=self.head

    def print(self):
        tmp=self.head
        if tmp is None:
            print('LinkedList is empty')
        else:
            while tmp:
                print(tmp.data, end=' ')
                tmp = tmp.next

obj = LinkedList()
arr=list(map(int,input().split()))
for i in arr:
    obj.Insert_at_start(i)
obj.print()
