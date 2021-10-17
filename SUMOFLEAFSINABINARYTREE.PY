class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

import queue
def takeinput():
    q=queue.Queue()
    print("ENTER THE VALUE OF ROOT : ")
    rootdata=int(input())
    if rootdata==-1:
        return None
    root=BinaryTree(rootdata)
    q.put(root)
    while (not(q.empty())):
        curr=q.get()
        print("ENTER THE VALUE OF LEFTCHILD OF",curr.data,": ")
        leftdata=int(input())
        if leftdata!=-1:
            leftchild=BinaryTree(leftdata)
            curr.left=leftchild
            q.put(leftchild)
        print("ENTER THE VALUE OF RIGHTCHILD OF",curr.data,": ")
        rightdata=int(input())
        if rightdata!=-1:
            rightchild=BinaryTree(rightdata)
            curr.right=rightchild
            q.put(rightchild)        
    return root

def leafs(root,leaf=[]):
    if root is None:
        return []
    if root.left==None and root.right==None:
        leaf.append(root.data)
    leafs(root.left,leaf)
    leafs(root.right,leaf)
    return leaf

def sumleaf(leafs):
    s=sum(leafs)
    return s
            
def printTree(root):
    if root==None:
        return
    inputq=queue.Queue()
    outputq=queue.Queue()
    inputq.put(root)
    while (not(inputq.empty())):
        while (not(inputq.empty())):
            curr=inputq.get()
            print(curr.data,end=" ")
            if curr.left!=None:
                outputq.put(curr.left)
            if curr.right!=None:
                outputq.put(curr.right)
        print()
        inputq,outputq=outputq,inputq

root=takeinput()
print("BINARY TREE IS :")
printTree(root)
leaf=leafs(root)
leafsum=sumleaf(leaf)
print("THE SUM OF LEAFS IN THE BINARY TREE IS :",leafsum)
print("LEAF IN THE BINARY TREE ARE :",end=" ")
if leaf==None:
    print("ZERO")
else:
    for i in leaf:
        print(i,end=" ")