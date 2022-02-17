## 4-2 ) Minimal Tree : Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

def createBST(arr):
    if not arr:
        return None

    mid_idx = len(arr) // 2
    mid_node = Node(arr[mid_idx])
    
    mid_node.left = createBST(arr[:mid_idx])
    mid_node.right = createBST(arr[mid_idx+1:])

    return mid_node