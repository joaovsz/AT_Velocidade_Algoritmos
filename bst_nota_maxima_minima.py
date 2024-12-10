class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def find_minimum(root):
    current = root
    while current.left is not None:
        current = current.left
    return current.val

def find_maximum(root):
    current = root
    while current.right is not None:
        current = current.right
    return current.val

notes = [85, 70, 95, 60, 75, 90, 100]
root = None
for note in notes:
    root = insert(root, note)

min_note = find_minimum(root)
max_note = find_maximum(root)

print(f"Nota mínima: {min_note}")
print(f"Nota máxima: {max_note}")