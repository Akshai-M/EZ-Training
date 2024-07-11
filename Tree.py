class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

def preorder(root):
    if root == None:
        return 
    print(root.data, "\n")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data, "\n")
    inorder(root.right)
def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, "\n")

if __name__ == "__main__":
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)
    # print(root/.data, root.left.data, root.right.data)

preorder(root)
inorder(root)
postorder(root)


