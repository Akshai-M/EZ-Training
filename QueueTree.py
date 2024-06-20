class Node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
#For preorder Root,Left,Right
def preorder(root):
    if root==None:
        return 
    print(root.value)
    preorder(root.left)
    preorder(root.right)
# Inorder Left,Root,Right
def inorder(root):
    if root==None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)
# Postorder Left Right Root
def postorder(root):
    if root==None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value)
def level_order(root):
    Q=[root]
    Q.append(None)
    while len(Q)!=0:
        curr=Q.pop(0)
        if curr==None:
            if len(Q)==0:
                break
            else:
                print()
                Q.append(None)
        else:
            print(curr.value,end=" ")
            if curr.left!=None:
                Q.append(curr.left)
            if curr.right!=None:
                Q.append(curr.right)



if __name__ =="__main__": 
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    root.left.right.left=Node(9)
    root.left.right.right=Node(10)
    root.right.right.left=Node(11)
    root.left.right.left.left=Node(12)
    root.left.right.left.right=Node(13)

# preorder(root)
# print("\n")
# postorder(root)
# print("\n")
# inorder(root)
level_order(root)