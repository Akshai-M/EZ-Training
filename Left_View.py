#               1
#            /    \
#           2      3
#            \      \
#             4      8
#            /        \
#           5          9
#          / \        /
#         6   7      10
#                   /
#                  11

class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

def left_view(root):
    q=[root]
    q.append(None)
    print(root.value)
    while len(q)!=0:
        c=q.pop(0)
        if c==None:
            if len(q)==0:
                return
            else:
                print(q[0].value)
                q.append(None)
        else:
            # print(c.value,end=' ')
            if c.left!=None:
                q.append(c.left)
            if c.right!=None:
                q.append(c.right)
        
if __name__=="__main__":
    root=node(1)
    root.left=node(2)
    root.right=node(3)


    # root.left.left=node(4)
    root.left.right=node(4)

    root.left.right.left=node(5)
    root.left.right.left.left=node(6)
    root.left.right.left.right=node(7)
    # root.left.right.right.right=node(13)

    root.right.right=node(8)
    root.right.right.right=node(9)
    root.right.right.right.left=node(10)
    root.right.right.right.left.left=node(11)
    

    # root.right.right.right=node(11)

left_view(root)