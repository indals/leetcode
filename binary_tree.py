class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def insert(self,val):
        if self.root is None:
            self.root = Node(val)
            return 
        curr = self.root
        while curr:
            if curr.val>val:
                if curr.left is None:
                    curr.left = Node(val)
                    return
                curr = curr.left
            if curr.val<val:
                if curr.right is None:
                    curr.right = Node(val)
                    return
                curr =  curr.right
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, end=' ')
    inorder(root.right)
def preorder(root):
    if root is None:
        return
    print(root.val, end=' ')
    inorder(root.left)
    inorder(root.right)
def postorder(root):
    if root is None:
        return
    inorder(root.left)
    inorder(root.right)
    print(root.val, end=' ')
def levelorder(root):
    if root is None:
        return
    q=[]
    q.append(root)
    while q:
        curr = q.pop(0)
        print(curr.val, end=' ')
        if curr.left is not None:
            q.append(curr.left)
        if curr.right is not None:
            q.append(curr.right)
def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right))+1
def helper(root,level,dict1):
    if root is None:
        return
    if dict1.get(level) is None:
        dict1[level]=root.val
    helper(root.left,level+1,dict1)
    helper(root.right,level+1,dict1)
    
def leftview(root):
    dict1={}
    helper(root,0,dict1)
    print('Left view of tree')
    for i in dict1:
        print(dict1[i], end=' ')
def helper(root, key,level,dict2):
    if root is None:
        return
    if dict2.get(key) is None:
        dict2[key]=[root,level]
    if dict2.get(key) is not None and dict2.get(key)[1]>level:
        dict2[key]=[root,level]
    helper(root.left, key-1,level+1,dict2)
    helper(root.right, key+1,level+1,dict2)
def topview(root):
    dict2={}
    helper(root,0,0,dict2)
    # print(dict2)
    for i in sorted(dict2):
        print(dict2[i][0].val, end=' ')
        
object=Tree()
lst = list(map(int,input('enter numbers').split()))
for i in range(len(lst)):
    object.insert(lst[i])
# print('Inorder')
# inorder(object.root)
# print()
# print('Preorder')
# preorder(object.root)
# print()
# print('Postorder')
# postorder(object.root)
# levelorder(object.root)
# print('Height of binary tree is {}'.format(height(object.root)))
# leftview(object.root)
topview(object.root)
