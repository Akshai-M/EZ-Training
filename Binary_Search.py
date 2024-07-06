class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = TreeNode(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = TreeNode(key)
            else:
                self._insert(root.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return self._search(root.left, key)
        return self._search(root.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.val:
            root.left = self._delete(root.left, key)
        elif key > root.val:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._min_value_node(root.right)
            root.val = temp.val
            root.right = self._delete(root.right, temp.val)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, root):
        result = []
        if root:
            result = self._inorder(root.left)
            result.append(root.val)
            result = result + self._inorder(root.right)
        return result

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("Inorder traversal of the BST:")
    print(bst.inorder())

    print("\nSearch for 40 in the BST:")
    result = bst.search(40)
    if result:
        print("Found:", result.val)
    else:
        print("Not Found")

    print("\nDelete 20 from the BST:")
    bst.delete(20)
    print("Inorder traversal after deletion:")
    print(bst.inorder())

    print("\nDelete 30 from the BST:")
    bst.delete(30)
    print("Inorder traversal after deletion:")
    print(bst.inorder())

    print("\nDelete 50 from the BST:")
    bst.delete(50)
    print("Inorder traversal after deletion:")
    print(bst.inorder())
