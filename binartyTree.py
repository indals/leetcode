class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def Insert_Iteration(self,val):
        if self.root is None:
            self.root=Node(val)
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
                    curr.right= Node(val)
                    return
                curr = curr.right
def height(root):
    if root is None:
        return 0
    return max(height(root.left),height(root.right))+1
def preOrder(root):
    if root is None:
        return
    print(root.val, end=' ')
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if root is None:
        return
    preOrder(root.left)
    print(root.val, end=' ')
    preOrder(root.right)
def postOrder(root):
    if root is None:
        return
    preOrder(root.left)
    preOrder(root.right)    
    print(root.val, end=' ')
def leftView(root,a,level):
    if root is None:
        return
    if a.get(level) is None:
        a[level]=root.val
    leftView(root.left,a,level+1)
    leftView(root.right,a,level+1)
def levelOrder(root):
    queue=[]
    if root is None:
        return 
    queue.append(root)
    while queue:
        tmp = queue.pop(0)
        print(tmp.val)
        if tmp.left is not None:
            queue.append(tmp.left)
        if tmp.right is not None:
            queue.append(tmp.right)
d={}
def topView(root,key,level):
    if root is None:
        return
    if key not in d:
        d[key] = [root, level]
    if d[key][1]>level:
        d[key]=[root,level]
    topView(root.left,key-1,level+1)
    topView(root.right,key+1,level+1)



object = BinaryTree()
lst = list(map(int,input().split()))
for i in lst:
    object.Insert_Iteration(i)
print('PreOrder')
preOrder(object.root)
print()
print('inOrder')
inOrder(object.root)
print()
print('PostOrder')
postOrder(object.root)
print(height(object.root))
a={}
level=0
print('Left veiw')
leftView(object.root,a,level)
print(a)
print()
print('Level order traversal:')
levelOrder(object.root)

topView(object.root,0,0)
# print(d)
for i in sorted(d):
    a=d[i][0]
    print(a.val, end=' ')



