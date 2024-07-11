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

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeData:
    def __init__(self, node, key):
        self.node = node
        self.key = key
def topview(root):
    if root is None:
        return
    
    q = [NodeData(root, 0)]  # Initialize queue with the root node at horizontal distance 0
    key_d = {}  # Dictionary to store the first node encountered at each horizontal distance

    while q:
        curr = q.pop(0)
        node = curr.node
        hd = curr.key
        
        # If this horizontal distance is being encountered for the first time
        # if hd not in key_d:
        key_d[hd] = node.value
        
        
        if node.left is not None:
            q.append(NodeData(node.left, hd - 1))
        
        
        if node.right is not None:
            q.append(NodeData(node.right, hd + 1))
    
    
    for hd in sorted(key_d):
        print(key_d[hd], end=' ')
    print()

# Test the implementation
if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.left.left = Node(9)
    root.right.right.left = Node(10)
    root.right.right.right = Node(11)
    root.right.right.left.left = Node(12)
    root.right.right.left.right = Node(13)
    
    topview(root)
