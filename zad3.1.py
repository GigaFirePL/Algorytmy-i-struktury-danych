class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def znajdz_sortowane(arr):
    kroki = 0
    kroki += 1
    min_val = arr[0]
    kroki += 1
    max_val = arr[-1]
    return min_val, max_val, kroki #Złożoność czasowa: O(1), pamięciowa: O(1)

def znajdz_niesortowane(arr):
    kroki = 0
    min_val = float('inf')
    max_val = float('-inf')
    for num in arr:
        kroki += 1
        if num < min_val:
            min_val = num
            kroki += 1
        if num > max_val:
            max_val = num
            kroki += 1 
    return min_val, max_val, kroki #Złożoność czasowa: O(n), pamięciowa: O(1)

def find_min_bst(node):
    kroki = 0
    while node.left is not None:
        kroki += 1
        node = node.left
    kroki += 1 
    return node.value, kroki #Złożoność czasowa: O(h), pamięciowa: O(1)

def find_max_bst(node):
    kroki = 0
    while node.right is not None:
        kroki += 1
        node = node.right
    kroki += 1
    return node.value, kroki #Złożoność czasowa: O(h), pamięciowa: O(1)

if __name__ == "__main__":
    Tablica_posortowana = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Tablica posortowana:", znajdz_sortowane(Tablica_posortowana))

    Tablica_nieposortowana = [3, 1, 4, 5, 2, 6, 0, -1, -2]
    print("Tablica nieposortowana:", znajdz_niesortowane(Tablica_nieposortowana))

    root = BSTNode(4)
    root.left = BSTNode(2)
    root.right = BSTNode(6)
    root.left.left = BSTNode(1)
    root.left.right = BSTNode(3)
    root.right.left = BSTNode(5)
    root.right.right = BSTNode(7)
    root.right.right.right = BSTNode(8)
    root.right.right.left = BSTNode(6)
    root.right.right.left.right = BSTNode(7)
    root.right.right.left.left = BSTNode(5)
    root.left.left.left = BSTNode(0)
    root.left.left.right = BSTNode(2)
    root.left.right.left = BSTNode(1)
    root.left.right.right = BSTNode(4)

    print("BST Min:", find_min_bst(root))
    print("BST Max:", find_max_bst(root))